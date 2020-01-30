from google.cloud import vision

def detect_faces_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')
    res = {}


    for i in range(len(faces)):
        res[i] = {}
        for face in faces:
            res[i]["confident"] = face.detection_confidence
            res[i]["joy"] = face.joy_likelihood
            res[i]["sorrow"] = face.sorrow_likelihood
            res[i]["anger"] = face.anger_likelihood
            res[i]["surprise"] = face.surprise_likelihood
            res[i]["under_exposed"] = face.under_exposed_likelihood
            res[i]["blurred"] = face.blurred_likelihood
            res[i]["headwear"] = face.headwear_likelihood

    temp = 0

    for key in list(res.keys()):
        for k in list(res[key]):
            temp = res[key][k]
            if res[key][k] > temp:
                temp = res[key][k]
        for k in list(res[key]):
            if res[key][k] == temp:
                del res[key][k]

    count = {'sorrow': 0, 'anger': 0, 'joy': 0, "surprise": 0, 'under_exposed':0,'blurred':0,'headwear':0 }
    for key in list(res.keys()):
        for k in list(res[key]):
            if k == "confident" and res[key][k] < .5:
                count['unsure'] = 100
            if k != "confident":
                count[k] = count[k] + 1
    temp = 0
    for key in list(count.keys()):
        if count[key] > temp:
            temp = count[key]
    for key in list(count.keys()):
        if count[key] != temp:
            del count[key]

    for key in list(count.keys()):
        if key == "under_exposed" or key == "blurred" or key == "headwear" or key == None or count[key] == 0 or key == "unsure":
            return "unsure"
        else:
            return key
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))