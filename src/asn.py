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
    returns = {}
    action = set()
    for sent in doc.sents:
        for token in sent:
            # print(f"token: {token},pos:{token.pos_}")
            head = token.head
            head_pos = head.pos_
            try:
                if str(head) != token.text:
                    returns[head].append(token)
                    if str(head_pos)=="VERB" or str(head_pos)=="ROOT" or str(head_pos)=="AUX":
                        action.add(head)
            except:
                if str(head) != token.text:
                    returns[head] = [token]
                    if str(head_pos)=="VERB" or str(head_pos)=="ROOT" or str(head_pos)=="AUX":
                        action.add(head)

    print(returns)
    for i in returns:
        print(returns[i])
        for j in returns[i]:
            print(j,j.pos_)
    print(f"action list: {action}")
    asn_list = []
    for i in action:
            for j in returns[i]:
                print(j)
            # asn_list.append(Asn(i,sub,obj))

    return returns

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
    sentence = "clouds floated above the sky"
    extract_dependency(sentence)
    svo(sentence)
    # sentence = convert_to_lemma(sentence)
    # result = extract_subject_object_verb(sentence)
    # print(result)

if __name__=="__main__":
    main()

