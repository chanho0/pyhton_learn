def calculate_sector(central_angle,radius):
    sector_area= central_angle / 360 * 3.14 * radius ** 2
    return(sector_area)
    

#calculate_sector(180,2)
print(f'扇形面积={calculate_sector(90,2)}')