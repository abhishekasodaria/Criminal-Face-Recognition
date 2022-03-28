import os
import shutil

import cv2
from dbHandler import *
from django.shortcuts import render
from facerec import *
from register import *
from register import *

from .forms import multi, ImageForm
from .models import Image


# Create your views here.
def show(request):
    return render(request, 'home.html')


'''def cri_reg(request):
	if request.method == 'POST':
		form = multi(request.POST)
		name = request.POST['Name']
		fathers = request.POST["FathersName"]
		mothers = request.POST["MothersName"]
		gender = request.POST["Gender"]
		dob = request.POST["DOB"]
		blood = request.POST["BloodGroup"]
		ident = request.POST["IdentificationMark"]
		nati = request.POST["Nationality"]
		rel = request.POST["Religion"]
		cri = request.POST["CrimesDone"]
		entry_data = {"Name":name,"FathersName":fathers,"MothersName":mothers,"Gender":gender,
						"DOB":dob,"BloodGroup":blood,"IdentificationMark":ident,"Nationality":nati
						,"Religion":rel,"CrimesDone":cri} 

		if form.is_valid():
			dirs = os.path.join('face_samples','temp_criminal')
			if not os.path.isdir(dirs):
				os.mkdir(dirs)
			no_face = []
			for i,img in enumerate(img_list):
				id = registerCriminal(img,dirs,i+1)
				
				if(id!=None):
					no_face.append(id)
				
			if len(no_face)>0:
				no_face_st = ''
				for i in no_face:
					no_face_st+='Image'+str(i)+','
					print("Registration Failed,Face too small")
					shutil.rmtree(dirs,ignore_errors = True)
			else:
				rowId = insertData(entry_data)

				if(rowId)>0:
					print("Criminal Registered Successfully")
					shutil.move(dirs,os.path.join('face_samples',entry_data["Name"]))
					return render(request,'home.html')
				else:
					shutil.rmtree(dirs,ignore_errors = True)
					print("Database Error")	

	else:
		filetype = [("images", "*.jpg *.jpeg *.png")]
		path_list =  filedialog.askopenfilenames(title = 'Choose atleast five images',filetypes = filetype)
		
		if len(path_list)<5:
			messagebox.showerror("Error", "Choose atleast 5 images.")
		else:
			
			for path in path_list:
				img_list.append(cv2.imread(path))
		form = multi()
		return render(request,'registration.html',{'form':form,"path_list":path_list})	# Create your views here.
'''


def detection(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = ImageForm(auto_id=True)
        print(form)
        return render(request, 'detection.html', {"form": form})


def image_list(request):
    header = "ImageData"
    image = Image.objects.all()
    return render(request, 'img_list.html', {'image': image})


def particular(request, pk):
    if request.method == "POST":
        j = Image.objects.get(pk=pk)
        pa = j.Image.path
        print(pa)
        img_read = cv2.imread(pa)
        crims_found_labels = []
        frame = cv2.flip(img_read, 1, 0)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_coords = detect_faces(gray_frame)

        if (len(face_coords) == 0):
            print("Image doesnt contain face")
        else:
            (model, names) = train_model()
            print("Training Successful. Detecting Faces")
            (frame, recognized) = recognize_face(model, frame, gray_frame, face_coords, names)

            frame = cv2.flip(frame, 1, 0)

            if (len(recognized) == 0):
                print("No Criminal Recognized")

            for i, crim in enumerate(recognized):
                return render(request, 'img_list.html', {"crim": crim[0], "j": j})


def open_image(request):
    if request.method == "POST":
        print(request.FILES["ImageField"])
        li = []
        l = []

        for f in request.FILES.getlist('ImageField'):
            imagename = 'C:/Users/Admin/Downloads/' + f.name
            l.append(imagename)
        for i in l:
            li.append(cv2.imread(i))

        name = request.POST['Name']
        fathers = request.POST["FathersName"]
        mothers = request.POST["MothersName"]
        gender = request.POST["Gender"]
        dob = request.POST["DOB"]
        blood = request.POST["BloodGroup"]
        ident = request.POST["IdentificationMark"]
        nati = request.POST["Nationality"]
        rel = request.POST["Religion"]
        cri = request.POST["CrimesDone"]
        entry_data = {"Name": name, "FathersName": fathers, "MothersName": mothers, "Gender": gender,
                      "DOB": dob, "BloodGroup": blood, "IdentificationMark": ident, "Nationality": nati
            , "Religion": rel, "CrimesDone": cri}

        form = multi(request.POST, request.FILES)

        if form.is_valid():
            dirs = os.path.join('face_samples', 'temp_criminal')
            if not os.path.isdir(dirs):
                os.mkdir(dirs)
            no_face = []
            for i, img in enumerate(li):
                id = registerCriminal(img, dirs, i + 1)

                if (id != None):
                    no_face.append(id)

            if len(no_face) > 0:
                no_face_st = ''
                for i in no_face:
                    no_face_st += 'Image' + str(i) + ','
                    print("Registration Failed,Face too small")
                    shutil.rmtree(dirs, ignore_errors=True)
            else:
                rowId = insertData(entry_data)

                if (rowId) > 0:
                    print("Criminal Registered Successfully")
                    shutil.move(dirs, os.path.join('face_samples', entry_data["Name"]))
                    return render(request, 'home.html')
                else:
                    shutil.rmtree(dirs, ignore_errors=True)
                    print("Database Error")

    else:
        forms = multi()
        print(forms)
        return render(request, 'registration.html', {"form": forms})
