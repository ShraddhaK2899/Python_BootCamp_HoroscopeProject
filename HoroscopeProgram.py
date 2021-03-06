# An Application Which Tells Future Based On The Zodiac Sign

#While Loop
next = True
while next==True:
#Print Syntax for Multi-Line Printing----------------------------
  print('''
  The Zodiac Signs Are:
  1) Aries
  2) Taurus
  3) Gemini
  4) Cancer
  5) Leo
  6) Virgo
  7) Libra
  8) Scorpio
  9) Sagittarius
  10) Capricorn
  11) Aquarius
  12) Pisces
  ''')


#Input Based On Zodiac Number------------------------------------
#But Now We Want Integer as Input - So We Do Typecasting.
#Input in Form of "String" needs to be typecasted to "Integer"
  s = int(input("From all the Zodiac Signs Pick Your Sign Number And Press Enter \n"))
  print("\n\nYour Input Zodiac Number is:") 
  print(s)
  print("\n\nThe Input Type is:") 
  print(type(s))  #Printing type of input we are getting



  print("\n\nYour Horoscope for Today is:")
  #Getting Horoscope Based on Zodiac Sign------------------------------
  if s==1:
      print("All eyes may be on you today — \nfor your looks, skills, or even your funky bag! Make hay while the sun shines, and charge your batteries \nwith all that attention. You can get some decent work done with \nthat energy.")
  elif s==2:
      print("Spontaneity yet sincerity will be\n the ruling emotions of the day. Keep your eyes and ears open, as trouble might be headed your way. Make \nit a point to read the print well before you sign any legal \ncontract today. Prevention is better than cure.")
  elif s==3:
      print("Today, your enthusiasm for sports and\n outdoor activities is palpable. According to you, variety is the spice of life. You will keep on jumping \nfrom one venture to another. It's time to taste success\n in your immediate and interim objectives.")
  elif s==4:
      print("It is likely that you will reach an \nimportant milestone in life today. Keep in mind that your success may be a cause of envy for a few people, \nsome of whom may want to harm you. You are left with \ntwo choices: either try to help them out of their troubles and miseries, or prepare for a battle.")
  elif s==5:
      print("Forget the weather. Today, the only thing\n shining bright are your chances of spending some quality time with your near and dear ones. Going along\n these lines, Ganesha wonders how long has it been \nsince you last did the same. So, make the most of this lucky day. Chances are that you shall make new friends, who might turn out to be very supportive in the future.")
  elif s==6:
      print("Business acumen is natural to you. Your \nmanagement skills are immaculate. Move with imagination, innovation and motivation to further your enterprise. \nFeel free to express and exercise your sense of judgement.")
  elif s==7:
      print("The whole point of being a Libran is that you always have\n the tendency to be two separate things put together on a pair of scales that somehow balance. \nGanesha feels that today, you'll bring to the scales the stability of being your own master and \nservant. It's a fine balance to maintain. But only you are capable of doing that, thanks to your extremely high-power status today.")
  elif s==8:
      print("Retail therapy with your loved ones is a perfect recipe to \nhave a good time! You will be more than willing to buy things of their choice. Haggling will be\n a trait you have closeted today as you go about being lavish in your expenses.")
  elif s==9:
      print("You may have women swooning over you today; such is your charm\n and way with them. But friends are highly valuable to you, and you shall spend much time with\n them cherishing their company and reliving amazing times spent together.")
  elif s==10:
      print("You love the people around you unconditionally and such emotions\n will be more visible now than ever. Today, you will want to keep yourself surrounded with your\n loved ones, make them happy and have a good time. Your honesty and sincerity will give depth\n to your existing relationships.")
  elif s==11:
      print("God helps those who help themselves. You have experienced this plenty\n of times as your efforts have been paid off. While your colleagues at work may pass \nnegative comments at your work, your boss will not have any complains with you. For investments \npurposes, real estate and construction seem to be a wise option.")
  elif s==12:
      print("You will be able to come up trumps against the competition today. You \nshould be wary of hidden enemies, for they might be involved in slandering you. It is \nbest to reach out to others and make friends before they take it upon themselves to hinder your \nprogress. Apart from this, no other significant event is indicated today.")
  else:
    print("\nHey! You sure about the number?")
  print("Have A Great Day!! :) ")

  
 #One-Liner For if-else Loop--------------------------------------------
  next = True if input("\n\n Would You  Like To Find Out Another Horoscope? (Y/N) \n")=="Y" else False
  print("Thanks For Finding Your Horoscope With Us!")
