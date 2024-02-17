
class Question:
    def __init__(self):
        self.score = 0
        self.question_bank = {}
        self.answer = ["a", "b", "a", "d", "c", "d", "d", "d", "c", "b", "a", "b", "a", "d", "c", "d", "d", "d", "c", "b"]



        self.question_prompts = [
   "What shape and colour is a warning sign?\n(a) Diamond Shape, Yellow and Black.\n(b) Circular, Red and White.\n(c) Triangular, Red and White.\n(d) Diamond Shape, Yellow and Black.\n\n" ,
   "What should a driver do when travelling downhill on snow or ice?\n(a) Avoid using the brake and use a high gear.\n(b) Select an appropriate gear and brake gently to control speed.\n(c) Keep close to the left and brake sharply to reduce speed.\n(d) Use a higher gear than normal in order to avoid wheel spin.\n\n" ,
   "In slow-moving city traffic, a driver should occasionally check their blind spots for which road users in particular?\n(a) Cyclists.\n(b) Taxis.\n(c) Vans.\n(d) Cars.\n\n" ,
   "What are the drink driving penalties for a professional driver holding a full car licence and found to have a blood alcohol concentrate (BAC) of 20 mg to 80 mg per 100 millilitres of blood?\n(a) €200 fine and 3 months driving disqualification.\n(b) There are no penalties below 50 mg (BAC).\n(c) The penalties only apply over 80 mg (BAC).\n(d) €100 fine and 6 months driving disqualification.\n\n" ,
   "Generally what lighting must a car, tractor or works vehicle have when driving?\n(a) Headlights, number plate and rear reflectors only.\n(b) Headlights, brake lights and indicators only\n(c) Headlights and a reversing light.\n(d) Headlights, front and rear side lights, rear number plate light, red rear reflectors, brake lights and indicators.\n\n" ,
   "What stopping distance should a driver allow for when driving in snow or icy conditions?\n(a) Up to half the normal distance.\n(b) The normal distance.\n(c) Up to ten times the normal distance.\n(d) Twice the normal distance.\n\n" ,
   "When should a driver use the vehicle side lights?\n(a) When driving in foggy conditions.\n(b) When driving in an unlit area at night.\n(c) When parking at all times.\n(d) When parking on an unlit road.\n\n" ,
   "When should a driver use dipped headlights?\n(a) From 00:00 hrs to 06:00 hrs.\n(b) When visibility is less than 300 metres.\n(c) When visibility is less than 200 metres.\n(d) From just after dusk to just before dawn.\n\n" ,
   "How can a pedestrian walking along a poorly lit road reduce the risk of an accident occurring?\n(a) Wear dark clothing.\n(b) Walk as part of a group.\n(c) Walk on the left-hand side of the road.\n(d) Wear high visibility clothing.\n\n" ,
   "What should drivers be aware of if they meet horses with riders on the road?\n(a) Horse riders are obliged to dismount and control their horses while traffic is passing.\n(b) All horse riders are experienced at handling horses.\n(c) Loud noises from their vehicle may frighten the horses and cause them to bolt.\n(d) Loud noises from their vehicle will not frighten the horses.\n\n" ,
   "What should a driver do when they intend to reverse into a side road?\n(a) Focus totally on the left side door mirror while reversing.\n(b) Check carefully all around before and during the reverse.\n(c) Open the left side door fully to look behind.\n(d) Angle the door mirrors down before reversing.\n\n" ,
   "What should a driver do when travelling on a motorway or dual carriageway?\n(a) Match the speed to that of the vehicle in the adjoining lane.\n(b) Be alert for other drivers who may suddenly change lanes or reduce speed.\n(c) Match the speed to that of the vehicle in front.\n(d) Relax because there will be no oncoming traffic.\n\n" ,
   "At a railway level crossing with unattended gates, what should a car driver do?\n(a) Drive halfway across and close the first gate before opening the second.\n(b) Open both gates and after passing the first, stop and close it.\n(c) Telephone the nearest railway station before opening a gate.\n(d) Open both gates before proceeding to cross.\n\n" ,
   "Who is responsible for ensuring that a passenger under 17 years of age is wearing a seat belt while travelling in a car?\n(a) The driver only.\n(b) The driver, but only when the passenger is in the front seat.\n(c) The passenger only.\n(d) The passenger’s parents.\n\n" ,
   "What should a driver do if there is very heavy traffic congestion in a tunnel?\n(a) Stop at the nearest emergency exit.\n(b) Switch on hazard warning lights.\n(c) Leave the vehicle.\n(d) Keep close to the vehicle in front.\n\n" ,
   "When approaching a roundabout, to whom should a driver give way?\n(a) The driver must only give way to heavy goods vehicles on the roundabout.\n(b) The driver approaching the roundabout always has right of way.\n(c) The driver must give way to traffic approaching from the right or already on the roundabout.\n(d) The driver must only give way to pedestrians and cyclists on the roundabout.\n\n" ,
   "When traffic lights are green, when should a driver not proceed?\n(a) When traffic is stopped waiting to turn from the road on the right.\n(b) When it would be unsafe to do so.\n(c) When traffic is stopped waiting to turn from the road on the left.\n(d) When oncoming traffic is waiting to turn left.\n\n" ,
   "When driving at night the full headlights of a typical car should enable the driver to see for a distance of how many metres?\n(a) 150 metres.\n(b) 100 metres.\n(c) 200 metres.\n(d) 50 metres.\n\n" ,
   "When attaching a trailer to their vehicle, what must a driver check?\n(a) That the load is positioned to the front of the trailer.\n(b) That the load is positioned to the rear of the trailer.\n(c) That the load is evenly spread.\n(d) That the trailer has a spare wheel.\n\n" ,
   "Can a child under the age of 3 years be carried unrestrained in the vehicle's front passenger seat?\n(a) No, unless the child is using a child booster seat.\n(b) Yes, provided the infant is held securely by an adult.\n(c) Yes, but only if the vehicle is fitted with active airbags.\n(d) No, an infant must always be restrained in the correct child seat.\n\n" ,
   "Where an injured person is discovered lying in the road, when should they be moved?\n(a) If the person has broken bones.\n(b) If the person needs CPR.\n(c) If the person is bleeding.\n(d) If the person is cold.\n\n"
]

    for i in range(len(self.question_prompts)):
        self.question_bank[self.question_prompts[i]] = self.answer[i]
'''
questions = [
    Question.Question(question_prompts[0], "a"),
    Question.Question(question_prompts[1], "b"),
    Question.Question(question_prompts[2], "a"),
    Question.Question(question_prompts[3], "a"),
    Question.Question(question_prompts[4], "d"),
    Question.Question(question_prompts[5], "c"),
    Question.Question(question_prompts[6], "d"),
    Question.Question(question_prompts[7], "d"),
    Question.Question(question_prompts[8], "d"),
    Question.Question(question_prompts[9], "c"),
    Question.Question(question_prompts[10], "b"),
    Question.Question(question_prompts[11], "b"),
    Question.Question(question_prompts[12], "b"),
    Question.Question(question_prompts[13], "a"),
    Question.Question(question_prompts[14], "b"),
    Question.Question(question_prompts[15], "c"),
    Question.Question(question_prompts[16], "b"),
    Question.Question(question_prompts[17], "c"),
    Question.Question(question_prompts[18], "c"),
    Question.Question(question_prompts[19], "d"),
    Question.Question(question_prompts[20], "b"),
    
]'''
    def run_test():
        for i in range(len(self.question_prompts)):
            answer = input(self.question_prompts[i]).lower()
            if answer == self.answer[i]:
                self.score += 1
                print("you got it correct:)\n\n")
            else:
                print("you got it wrong :(\n\n")
                
        print(f"Your score is: {self.score}/{len(questions)} [{round (self.score/len(self.question_prompts)*100,2)}%] ".format())
        
