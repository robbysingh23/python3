hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

check = input("Would you like to check in or check out? ").lower()
in_out = input("What is the floor and room number? ")

if check == 'check in':
  num_name_occ = input("How many occupants and their names? ")
elif check == 'checkout':

# is room occupied? function
def vacancy():
  for 