def trip_planner_welcome(name):
  print('Welcome to tripplanner v1.0 ' + name)

  trip_planner_welcome("Moe")


def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time, 20)
  return rounded_time

estimate = estimated_time_rounded(20)

def destination_setup(origin, destination,  estimated_time, mode_of_transport='Boat'):
  print('Your trip starts off in ' + origin)
  print('And you are traveling to  ' + destination)
  print('You will be traveling by ' + mode_of_transport)
  print('It will take approximately ' + str(estimated_time) + 'hours')

  destination_setup("Texas", "Japan ", estimate, "Boat"


