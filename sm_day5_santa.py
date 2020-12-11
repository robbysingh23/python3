item = input("What item would you like for christmas: ")
good_bad = input("Have you been good or bad?: ").lower()

if good_bad == 'good':
  print("Since you've been so good, you get to have a %s" % (item))
elif good_bad == 'bad':
  print("Whoops, looks like you've been a bad boy, you do not get a %s" % (item))
else:
  print("Please use the word Good or Bad while answering me")