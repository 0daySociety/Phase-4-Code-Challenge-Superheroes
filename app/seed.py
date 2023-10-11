#!/usr/bin/env python3
from models import  Power,Hero,Hero_Power,db
from app import app 
import random
with app.app_context():

  try:
    Power.query.delete()
    Hero.query.delete()
    Hero_Power.query.delete()

      
    power_1 =Power(
      name="super strength", description="gives the wielder super-human strengths"
    )
    power_2=Power(
      name= "flight", description= "gives the wielder the ability to fly through the skies at supersonic speed"
    )
    power_3 =Power(
      name= "super human senses", description= "allows the wielder to use her senses at a super-human level")
    power_4 =Power(
      name= "elasticity", description= "can stretch the human body to extreme lengths" )
    power_list =[power_1,power_2,power_3,power_4]

    db.session.add_all(power_list)
  
  except Exception as e:
    print("we got this error",str(e))
  hero_1 =Hero(
    name= "Kamala Khan", super_name= "Ms. Marvel"

  )
  hero_2 =Hero(
    name= "Doreen Green", super_name= "Squirrel Girl"
  )
  hero_3 =Hero(
    name= "Gwen Stacy", super_name= "Spider-Gwen"  
  )
  hero_4=Hero(
      name= "Janet Van Dyne", super_name= "The Wasp"
  )
  hero_5 =Hero(
    name= "Wanda Maximoff", super_name= "Scarlet Witch" 
  )

  hero_6=Hero(
    name="Carol Danvers", super_name= "Captain Marvel"
  )


  hero_7 =Hero(
    name= "Jean Grey", super_name= "Dark Phoenix"
  )

  hero_8=Hero(
      name="Ororo Munroe", super_name= "Storm"
  )

  hero_9=Hero(
      name= "Kitty Pryde", super_name= "Shadowcat" 

  )

  hero_10=Hero(
      name= "Elektra Natchios", super_name= "Elektra" 
  )

  hero_list=[hero_1,hero_2,hero_3,hero_4,hero_5,hero_6,hero_7,hero_8,hero_9,hero_10]
  try:

    db.session.add_all(hero_list)
    db.session.commit()
  except Exception as e:
    print("we got this error ", str(e))






  strengths = ["Strong", "Weak", "Average"]
  hero_power_lists=[]
  for i in range(10):
   
  
    
    hero_test=hero_list[random.randint(0,len(hero_list)-1)]
    hero_my_id =hero_test.id

    power_test =power_list[random.randint(0,len(power_list)-1)]
    power_my_id =power_test.id
    hero_power =Hero_Power(
      strength=strengths[random.randint(0,len(strengths)-1)],
      hero_id =hero_my_id,
      power_id =power_my_id
    )
    hero_power_lists.append(hero_power)
   
  db.session.add_all(hero_power_lists)
  db.session.commit()  
  
 





 



# Hero.create([
#   { name= "Kamala Khan", super_name= "Ms. Marvel" },
#   { name= "Doreen Green", super_name= "Squirrel Girl" },
#   { name= "Gwen Stacy", super_name= "Spider-Gwen" },
#   { name= "Janet Van Dyne", super_name= "The Wasp" },
#   { name= "Wanda Maximoff", super_name= "Scarlet Witch" },
#   { name= "Carol Danvers", super_name= "Captain Marvel" },
#   { name= "Jean Grey", super_name= "Dark Phoenix" },
#   { name= "Ororo Munroe", super_name= "Storm" },
#   { name= "Kitty Pryde", super_name= "Shadowcat" },
#   { name= "Elektra Natchios", super_name= "Elektra" }
# ])




# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(=id).sample)

#     Hero_Power.create!(hero_id= hero.id, power_id= power.id, strength= strengths.sample)



