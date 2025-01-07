#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep

class LaLigaMR(MRJob):
        
    # Mapper: Extraemos goles de cada equipo en casa y fuera
    def mapper(self, _, line):
        # Extraemos las columnas necesarias (asegurándonos de saltar las cabeceras)
        _, _, _, home_team, away_team, home_goals, away_goals, *rest = line.split(',')
        
        # Si la línea es la cabecera, no la procesamos
        if home_team == "HomeTeam":
            return

        # Emitimos los goles marcados por cada equipo
        yield home_team, int(home_goals)  # Goles de casa
        yield away_team, int(away_goals)  # Goles de visitante
        
    # Combiner: Suma de los goles de cada equipo (para reducir la cantidad de datos enviados al reducer)
    def combiner(self, team, goals):
        yield team, sum(goals)
    
    # Reducer: Sumamos los goles por equipo y encontramos los equipos con más y menos goles
    def reducer(self, team, goals):
        total_goals = sum(goals)
        yield None, (team, total_goals)

    # Reducer final para ordenar los resultados y calcular la diferencia de goles
    def reducer_final(self, _, teams_goals):
        sorted_teams = sorted(teams_goals, key=lambda t: t[1], reverse=True)
        
        # El primer equipo tiene la mayor cantidad de goles y el último la menor cantidad
        max_goals_team = sorted_teams[0]
        min_goals_team = sorted_teams[-1]
        
        # Calculamos la diferencia de goles
        diff_goals = max_goals_team[1] - min_goals_team[1]
        
        yield f"{max_goals_team[0]} vs {min_goals_team[0]}", f'diferencia de goles {diff_goals}'

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_final)
        ]
         
if __name__=='__main__':
    LaLigaMR.run()
