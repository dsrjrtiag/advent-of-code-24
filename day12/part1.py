from dataclasses import dataclass
from typing import Self
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

@dataclass
class Plant:
    x: int
    y: int
    plant: str
    perimeter = 0
    def __hash__(self):
        return ord(self.plant) + self.x * self.y 
    
    def plants_around(self, plot: list[list[Self]]) -> list[Self]:
        max_coord: int = len(plot) - 1
        plants = []
        perimeter = 0
        if self.x > 0:
            plant = plot[self.y][self.x - 1]
            if plant.plant == self.plant:
                plants.append(plant)
            else:
                perimeter += 1 
        else:
            perimeter += 1
        if self.x < max_coord:
            plant = plot[self.y][self.x + 1]
            if plant.plant == self.plant:
                plants.append(plant)
            else:
                perimeter += 1 
        else:
            perimeter += 1
        if self.y > 0:
            plant = plot[self.y - 1][self.x]
            if plant.plant == self.plant:
                plants.append(plant)
            else:
                perimeter += 1 
        else:
            perimeter += 1
        if self.y < max_coord:
            plant = plot[self.y + 1][self.x]
            if plant.plant == self.plant:
                plants.append(plant)
            else:
                perimeter += 1 
        else:
            perimeter += 1

        self.perimeter = perimeter
        return plants

def get_plot(plant: Plant, field: list[list[Plant]], added: set[Plant]):
    added.add(plant)
    plot = [plant]
    plants_around = plant.plants_around(field)
    for around_plant in plants_around:
        if around_plant not in added:
            added.add(around_plant)
            plot.extend(get_plot(around_plant, field, added))
    return plot

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    plants: list[list[Plant]] = []
    for y in range(len(input_lines)):
        row = []
        for x in range(len(input_lines[y])):
            row.append(Plant(x, y, input_lines[y][x]))
        plants.append(row)

    processed_plants: set[Plant] = set()
    plant_plots: list[list[Plant]] = []
    for row in plants:
        for plant in row:
            if plant not in processed_plants:
                plant_plot = get_plot(plant, plants, processed_plants)

                processed_plants.update(plant_plot)
                plant_plots.append(plant_plot)
    
    total_score = 0
    for plot in plant_plots:
        area = len(plot)
        permimeter = sum([plant.perimeter for plant in plot])
        score = area * permimeter
        total_score += score
    print(total_score)

def main():
    run()

if __name__=="__main__":
    main()