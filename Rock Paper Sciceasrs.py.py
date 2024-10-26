#rock paper scicors 
def gamer():
  
    import random 
    
    name =input(str("Enter your name \n"))
    usert=int(input("enter the number of life for user and computer\n"))
    compt=usert
    print("---you have ",usert," life and the computer has ",compt," life also---\n <<GAME STARTED>>")
    print("--press q to exit the game\n")
   
    f=["rock","paper","sciscors"]

    while usert and compt!=0:
    
      x= input("--choose rock paper sciscors?\n\n ")
      
      z=random.choice(f)
      if x=="rock":
             if x==z:
               print ("computer '-':\n <--",z,"-->",name, "draw")
             elif z=="paper":
               print ("computer :):\n <--",z,"-->",name, "lose")
               usert=usert-1
               print("the user life =",usert,"the computer life =",compt)
             elif z=="sciscors":
               print("computer 0_0:\n <--",z,"-->",name, "win!")
               compt=compt-1
               print("the user life =",usert,"the computer life =",compt)
      elif x=="paper":
             if x==z:
               print ("computer '-':\n <--",z,"-->",name, "draw")
             elif z=="rock":
               print ("computer :):\n <--",z,"-->",name, "win!")
               compt=compt-1
               print("the user life =",usert,"the computer life =",compt)
             elif z=="sciscors":
               print("computer 0_0:\n <--",z,"-->",name, "lose!")
               usert=usert-1
               print("the user life =",usert,"the computer life =",compt)
      elif x=="sciscors":
             if x==z:
               print ("computer '-':\n <--",z,"-->",name, "draw")
             elif z=="rock":
               print ("computer :):\n <--",z,"-->",name, "lose!")
               usert=usert-1
               print("the user life =",usert,"the computer life =",compt) 
             elif z=="paper":
               print("computer 0_0:\n <--",z,"-->",name, "win!")
               compt=compt-1
               print("the user life =",usert,"the computer life =",compt)
      elif x=="q":
            print("closing the game")
            break
            
      elif x!=f:
            print("worng input Try again")
            
      else :
            print("wrong input")
            break
            
    if usert==0:
      print("\n\n------YOU Have lost------ \n------GAME OVER------")
      r=input(str("\n press -W- to play again?\n press -Z- to exit the game\n"))
      if r=="w":
        print("<<<<new game wp>>>>")
  
        gamer()
      elif r=="z":
         print("closing the game GG")
         exit
      else:
          print("wrong input")
          
          
    elif compt==0:
     print("\n\n------Your Winner------ \n ------NICE TRY------")
     r=input(str("\n press -W- to play again?\n press z to exit the game\n"))
     if r=="w":
        print("<<<<new game wp>>>>")
        
        gamer()
     elif r=="z":
         print("closing the game GG")
         exit
     else:
          print("wrong input")       
gamer()

