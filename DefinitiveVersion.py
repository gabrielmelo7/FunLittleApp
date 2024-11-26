from deepface import DeepFace
import cv2
import uuid
import os

#The function for capturing the images 
def img_capture(directory):

    #Initializing the webcam
    cap = cv2.VideoCapture(0)
    while cap.isOpened():

        ret, frame = cap.read()
        cv2.imshow("Frame", frame)

        #Saving a photo of the image captured in the webcam
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_name = os.path.join(directory, '{}.jpg' .format(uuid.uuid1()))
            cv2.imwrite(img_name, frame)
            break

        #Ending without taken photos
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    #Returning the captured images
    return img_name
    
def img_save(directory, image):
    img_path = os.path.join(directory, '{}.jpg' .format(uuid.uuid1()))
    cv2.imwrite(img_path, image)

    return img_path

#The function that evaluates the captured image
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

#Simple functions that gives us our result.    

def main():

    #Local directory that stores our taken photos
    directory = "TestPhotos"
    #Arbitrary reference image from our TestPhotos folder
    reference_img = os.path.join(directory, "104ca980-aacd-11ef-bd34-3c219c5ea82f.jpg")

    #Calling the functions in the order they are supposed to work
    image = img_capture(directory)
    result = img_verification(image, reference_img)
    img_evaluation(result)


if __name__ == "__main__":
    main()





    




        
