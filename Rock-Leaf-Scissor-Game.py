#           ---------------Rock , Leaf , Scissor Game---------------
from random import randint
print("\n\n\n\t\t\t\t\t\tRock vs Leaf vs Scissor Game\n\n\n")
username = input("Enter Your Username >>: ")
user_score = 0
pc_score = 0
drawn = 0
while True:
    print(f"\t\t\t\t\t\t{username} score: {user_score} | drawn: {drawn} | pc score: {pc_score}\n\n")
    print("\nChoose one of Three\n1.Rock\n2.Leaf\n3.Scissor\n4.Quit")
    tool = input("\n>>: ")
    tool_pc = randint(1,3)
    if tool_pc == 1:
        tool_pc = "Rock"
    elif tool_pc == 2:
        tool_pc = "Leaf"
    else: tool_pc = "Scissor"
    
    if tool.lower() == "quit" or tool.lower() == "q" or tool == 4:
        print("\n\n\t\t\tYou Quit The Game\n\n")
        break
    elif tool.lower() == tool_pc.lower():
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        drawn+=1
        print("\t\t\t Null Match \n")
    elif tool.lower() == "rock" and tool_pc.lower() == "leaf":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        pc_score+=1
        print("\t\t\tPc Win\n")
    elif tool.lower() == "rock" and tool_pc.lower() == "scissor":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        user_score+=1
        print("\t\t\tYou Win\n")
    elif tool.lower() == "leaf" and tool_pc.lower() == "rock":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        user_score+=1
        print("\t\t\tYou Win\n")
    elif tool.lower() == "leaf" and tool_pc.lower() == "scissor":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        pc_score+=1
        print("\t\t\tPc Win\n")
    elif tool.lower() == "scissor" and tool_pc.lower() == "rock":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        pc_score+=1
        print("\t\t\tPc Win\n")
    elif tool.lower() == "scissor" and tool_pc.lower() == "leaf":
        print(f"\n\n\t\t\t{tool.capitalize()}  VS  {tool_pc}\n\n")
        user_score+=1
        print("\t\t\tYou Win\n")
    else: continue
if user_score > pc_score:
    print("\t\t\t\t\t\t\tohho YOU Win !!\n\n")
elif user_score < pc_score:
    print("\t\t\t\t\t\t\t\tPC Win !!\n\n")
else: print("\n\n\t\t\t\t\t\t\t\tDRAWN !!\n\n")
print("\t\t\t\t----------------------------------------------------------------\n")
print(f"\t\t\t\t\t\t{username} score: {user_score} | drawn: {drawn} | pc score: {pc_score}")
print("\n\t\t\t\t----------------------------------------------------------------\n\n")
  
