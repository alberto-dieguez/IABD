#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
    
class laligaMRLast5Matches(MRJob):

    # Mapper: En esta etapa aún no hay clave (_), el valor lo recibimos en la variable line
    def mapper_points(self, _, line):
        # Por cada línea, esta se divide en los campos que forman las columnas
        _, date, _, home_team, away_team, _, _, result, *rest = line.split(',')
        
        # Si es la cabecera no emitimos nada
        if home_team == "HomeTeam":
            return
        
        # Convertir la fecha para ordenar correctamente
        date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y/%m/%d")
        
        # Emitimos la fecha y los puntos para cada equipo
        if result == 'D':            
            yield home_team, (date, 1)
            yield away_team, (date, 1)
        elif result == 'H':
            yield home_team, (date, 3)
            yield away_team, (date, 0)
        else:
            yield home_team, (date, 0)
            yield away_team, (date, 3)
            
    def combiner_points(self, team, values):
        # Combina los puntos y fechas por equipo
        combined_points = list(values)
        yield team, combined_points
            
    def reducer_points(self, team, values):
        # Aplanamos y ordenamos por fecha
        all_games = sorted([item for sublist in values for item in sublist], key=lambda x: x[0])

        # Obtenemos los puntos de los últimos 5 partidos
        last_five_points = [points for date, points in all_games[-5:]]
        last_five_points.reverse()
        # Calculamos el total de puntos
        total_points = sum(points for date, points in all_games)

        yield None, (team, total_points, last_five_points)
    
    def reducer_classification(self, _, points):
        # Ordenamos los equipos por los puntos totales
        yield None, sorted(points, key=lambda t: t[1], reverse=True)
            
    def steps(self):
        return [
            MRStep(mapper=self.mapper_points,
                   combiner=self.combiner_points,
                   reducer=self.reducer_points),
            MRStep(reducer=self.reducer_classification)
        ]
         
if __name__=='__main__':
    laligaMRLast5Matches.run()



