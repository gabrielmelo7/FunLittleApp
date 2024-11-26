from deepface import DeepFace

def img_verification(img, reference):
    print(reference)
    try:
        #Using VGG-Face from DeepFace. 
        result = DeepFace.verify(img, reference, model_name="VGG-Face")
        #Result is a dictionary, we wish to acess the 'verified' area of the dictionary
        is_img = result['verified']
        return is_img
    
    #Catching potential excepctions
    except Exception as e:
        return False






    




        
