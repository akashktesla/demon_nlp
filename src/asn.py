#import
import spacy
#load the model
nlp = spacy.load("en_core_web_sm")


def extract_subject_object_verb(text):
    doc = nlp(text)
    
    results = []

    for sent in doc.sents:
        subj = []
        obj = []
        verb = []

        for token in sent:
            print(token,token.dep_)
            # Extract subject
            if "subj" in token.dep_:
                subj.append(token.text)
            
            # Extract object
            if "obj" in token.dep_:
                obj.append(token.text)
            
            # Extract verb
            if "VERB" in token.pos_:
                verb.append(token.text)
        
        results.append((subj, verb, obj))
    
    return results

def convert_to_lemma(text):
    doc = nlp(text)
    lemma_doc = " ".join(token.lemma_ for token in doc)
    return lemma_doc

class Asn():
    def __init__(self,action,subject,obj):
        self.action = action
        self.subject = subject
        self.obj = obj



def extract_dependency(text):
    doc = nlp(text)
    head_map = {}
    tail_map = {}
    action = set()
    for sent in doc.sents:
        for token in sent:
            print(f"token: {token},pos:{token.pos_}")
            head = token.head
            tail_map[token] = head
            head_pos = head.pos_
            try:
                if str(head) != token.text:
                    head_map[str(head.text)].append(token.text)
                    if str(head_pos)=="VERB" or str(head_pos)=="ROOT" or str(head_pos)=="AUX":
                        action.add(head.text)
            except:
                if str(head) != token.text:
                    head_map[str(head.text)] = [token.text]
                    if str(head_pos)=="VERB" or str(head_pos)=="ROOT" or str(head_pos)=="AUX":
                        action.add(head.text)
    # print(f"action list: {action}")
    print(f"head map: {head_map}")
    # print(f"tail_map: {tail_map}")
    for i in head_map:
        print(return_arn(i,head_map))
    # print(head_map["eager"])
    # for i in head_map:
    #     print(f"key: {i}")
    #     print(f"value: {head_map[i]}")



def return_arn(func,head_map):
    # print("return_arn initialized")
    param = head_map[func]
    try: 
        a = return_arn(param[0],head_map)
    except:
        a = param[0]

    for i in param[1:]:
        # if not i in [",","."]:
            # print(f"i: {i}")
            try:
                b = return_arn(i,head_map)
                # print(f"bla: {head_map[i]}")
                # print(f"b: {b}")
                a = f"{a}, {b}"
            except: 
                a = f"{a}, {i}"
    return f"{func}({a})"




def svo(text):
    verb = []
    noun = []
    doc = nlp(text)
    for sent in doc.sents:
        for token in sent:
            pos = token.pos_
            if pos in ["VERB","ROOT","AUX"]:
                verb.append(token)
            elif pos in ["NOUN"]:
                noun.append(token)
        print(f"verb: {verb}")
        print(f"noun: {noun}")




def main():
    # sentence = "clouds floated above the sky"
    # sentence = "Sparkling stars danced across the velvet night sky"
    # sentence = "The aroma of freshly baked bread filled the cozy kitchen."
    # sentence = "The curious cat explored the garden, chasing after fluttering butterflies."
    # sentence = "The book is in the shelf"
    # sentence = "After a long day at work, Akash enjoyed a relaxing evening by experimenting with AI in Python."
    # sentence = "Rust's efficient memory management makes it a powerful choice for developing robust software applications."
    # sentence = "Under the starlit sky, the campfire crackled, warming the chilly night."
    # sentence = "With a map in hand, they ventured into the dense forest, eager for an adventure."
    sentence = "I love red apples,coffee shop,juicy oranges"

    extract_dependency(sentence)
    svo(sentence)
    # sentence = convert_to_lemma(sentence)
    # result = extract_subject_object_verb(sentence)
    # print(result)

if __name__=="__main__":
    main()

