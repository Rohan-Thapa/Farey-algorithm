'''
Lorentz Factor,
velocity_of_person(v), speed of the light(c),

LF(γ) = 1 / ((1 - ((v^2) / (c^2))) ^ (1/2))

Relative acceleration to time,
time Δt (in the crew’s frame) and Δv for difference in velocity or the v of above,
a = Δv / Δt
the t should be time in second and v should be in m/s

So the proper acceleration becomes,
α = γ^3 ⋅ a

And the G-Force becomes,
G-Force = α / g  (For earth it is 9.8 for the g so it gets relative to earth g if it was different than relative to that it comes.)
'''

#!/bin/python3
print("The velocity should be in the factor to c, such as 0.1c or 1c or something...")
final_velocity: float = float(input("Enter the final crusing velocity: "))

print("Which time unit you want to use seconds(s), minutes(m), hours(h), days(d), months(mn), years(y)")
time_unit: str = input("Enter the unit you want to use: ").lower()

sec_time: int = 1
min_time: int = sec_time * 60
hour_time: int = min_time * 60
day_time: int = hour_time * 24
month_time: int = day_time * 30
year_time: int = month_time * 12

print("The time should be relative to the crew inside the ship not relative to Earth as there will be time dialation between two.")
time_value: int = int(input("Enter the amount of time required to get that speed: "))

if time_unit == 's':
    time = time_value * sec_time
elif time_unit == 'm':
    time = time_value * min_time
elif time_unit == 'h':
    time = time_value * hour_time
elif time_unit == 'd':
    time = time_value * day_time
elif time_unit == 'mn':
    time = time_value * month_time
elif time_unit == 'y':
    time = time_value * year_time
else:
    print("There was some error in the value provided above... Quitting the program")
    quit()

print("Enter the value of g with which ration you want to find for the earth the value is 9.8 and G force will be related to it but other value could also taken as the reference also.")
g_value: float = float(input("Enter the value of g: "))

c_value = 3*10**8  # the speed of light in m/s

LF: float = 1 / ((1 - final_velocity ** 2) ** (1/2))

a_coord: float = (final_velocity * c_value) / time

relative_acceleration = (LF ** 3) * a_coord

G_Force = relative_acceleration / g_value

print(f"The relative G-Force experienced by the crew during acceleration of the ship for the following condition is {round(G_Force, 3)} G.")
