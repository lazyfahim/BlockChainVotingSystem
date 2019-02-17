import json
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import hashlib
import os

# import sys
# sys.path.append("..")

mydict = {}




class BlockChain:


    # Initialized data
    def __init__(self):
        self.previousHash = None
        self.pres = []
        self.vp = []
        self.sec = []

        self.pres_nom = []
        self.vp_nom = []
        self.sec_nom = []

        self.pres_final_cnt = []
        self.vp_final_cnt = []
        self.sec_final_cnt = []


    # hash the block to check
    def hash_block(self, electionID, voterID, block_type, data):

        vote_data = {
            "elec_id": electionID,
            "voter_id": voterID,
            "block_type": block_type,
            block_type + "_data": data,
            "prev_hash": self.previousHash
        }

        vote_serialized = json.dumps(vote_data).encode('utf-8')
        vote_hashed = hashlib.sha256(vote_serialized).hexdigest()
        self.previousHash = vote_hashed
        return vote_serialized

    
    # Add vote block to our channel
    def add_vote_block(self, elec_id, voter_id, vote_data):
        
        mydict[elec_id] = []

        a = []
        for i in range(0, 6):

            mydict[elec_id].append(a)

        file_name = elec_id + '.json'

        if os.path.exists(file_name):
            print("yes")
        else:
            f = open(file_name, 'w+')
            f.write('[]')
            f.close()

        hash_data = self.hash_block(elec_id, voter_id, "vote", vote_data).decode("utf-8")
        hash_data_json = json.loads(hash_data)

        file = open(file_name, 'r')
        file_data = file.read()
        file_data_json = json.loads(file_data)
        file.close()

        data = file_data_json + [hash_data_json]
        file = open(file_name, 'w')
        file.write(json.dumps(data))
        file.close()

        file = open(file_name, 'r')
        new_file_data = file.read()
        new_file_data_json = json.loads(new_file_data)
        file.close()
        # print(new_file_data_json)

        for i in range(0, len(new_file_data_json)):
            tmp = new_file_data_json[i]['vote_data']
            n = len(tmp)

            for j in range(0, n):
                print(tmp[j])

                # print(" he ")
                temp = tmp[j][1]

                print("voted ", tmp[j][0], type(tmp[j][0]))

                if tmp[j][0] == "-1":
                    continue

                if temp == "pres":
                    self.pres.append(tmp[j][0])

                elif temp == "vice":
                    self.vp.append(tmp[j][0])

                elif temp == "sec":
                    self.sec.append(tmp[j][0])

            print("\n")
            print(self.pres, self.vp, self.sec)
            print("\n")

            pres_cnt = []
            vp_cnt = []
            sec_cnt = []

            myset = set(self.pres)
            print(myset)
            for i in myset:
                # print('i = ', i)
                val = self.pres.count(i)
                pres_cnt.append(tuple((i, val)))

            print("pres-cnt = ", pres_cnt)

            myset = set(self.vp)
            for i in myset:
                val = self.vp.count(i)
                vp_cnt.append(tuple((i, val)))

            print("vp-cnt = ", vp_cnt)

            myset = set(self.sec)
            for i in myset:
                val = self.sec.count(i)
                sec_cnt.append(tuple((i, val)))

            print("sec-cnt = ", sec_cnt)

            self.pres_final_cnt = pres_cnt
            self.vp_final_cnt = vp_cnt
            self.sec_final_cnt = sec_cnt

        mydict[elec_id][3] = self.pres_final_cnt

        print(mydict[elec_id][3])

        mydict[elec_id][4] = self.vp_final_cnt
        mydict[elec_id][5] = self.sec_final_cnt


        with open('result.json','w') as fp:
            json.dump(mydict,fp)


        return True

    # Add num block to our channel
    def add_nom_block(self, elec_id, voter_id, nom_data):
       
        mydict[elec_id] = []

        a = []
        for i in range(0, 6):

            mydict[elec_id].append(a)

        file_name = elec_id + 'nom.json'

        if os.path.exists('voting/' + file_name):
            print("yes")
        else:
            f = open('voting/' + str(file_name), 'w+')
            f.write('[]')
            f.close()

        hash_data = self.hash_block(elec_id, voter_id, "nom", nom_data).decode("utf-8")
        hash_data_json = json.loads(hash_data)

        file = open('voting/' + str(file_name), 'r')
        file_data = file.read()
        file_data_json = json.loads(file_data)
        file.close()

        data = file_data_json + [hash_data_json]
        file = open('voting/' + file_name, 'w')
        file.write(json.dumps(data))
        file.close()

        file = open('voting/' + file_name, 'r')
        new_file_data = file.read()
        new_file_data_json = json.loads(new_file_data)
        file.close()

        print(new_file_data_json)

        print(" new_file_data_json length =  ", len(new_file_data_json))

        for i in range(0, len(new_file_data_json)):
            tmp = new_file_data_json[i]['nom_data']
            # print("ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
            for j in range(0, len(tmp)):
                temp = tmp[j][1]

                # print("hello ", i, j)

                print(temp)

                print(tmp[j][0])

                print(self.pres_nom, self.vp_nom, self.sec_nom)

                if tmp[j][0] == "-1":
                    # print("hello 111111111111111111", i, j)
                    continue

                if temp == "pre" and tmp[j][0] not in self.pres_nom:
                    self.pres_nom.append(tmp[j][0])

                    # print("=====================", j, self.pres_nom)

                elif temp == "vice" and tmp[j][0] not in self.vp_nom:
                    self.vp_nom.append(tmp[j][0])

                    print("!!!!!!!!!!!!!!", j, self.vp_nom)

                elif temp == "sec" and tmp[j][0] not in self.sec_nom:
                    self.sec_nom.append(tmp[j][0])

                    # print("+++++++++++++++++++===", j, self.sec_nom)

            print("\n")
            print(self.pres_nom, self.vp_nom, self.sec_nom)

        mydict[elec_id][0] = self.pres_nom
        mydict[elec_id][1] = self.vp_nom
        mydict[elec_id][2] = self.sec_nom

        with open('result.json','w') as fp:
            json.dump(mydict,fp)

        return True


blockchain = BlockChain()



# Check if a nominee is valid
def check_nominee(inputList, elec_id, voter_id):
    found = False
    prevHash = None
    missing = True
    for record in inputList:
        # print(record)
        # if prevHash != record["prev_hash"]:
            # found = True
            # break
        if record["elec_id"] != elec_id:
            continue
        elif record["voter_id"] != voter_id:
            continue
        else:
            missing = False
            break
    return missing


# Check if a voter is valid
def check_voter(self, inputList, inputRecord):
    missing = True
    for record in inputList:
        # if prevHash != record["prev_hash"]:
            # found = True
            # break
        if record["elec_id"] != inputRecord["elec_id"]:
            continue
        elif record["voter_id"] != inputRecord["voter_id"]:
            continue
        else:
            missing = False
            break
    return missing


# to get the result of nominateed registered  user
class CheckNom(APIView):


    def get(self, request, election_id, voter_id, format=None):
        input_data = request.data

        file_name = '' + election_id + 'nom.json'

        if os.path.exists('voting/' + file_name):
            with open('voting/' + file_name, 'r') as f:
                print('voting/' + file_name)
                txt_data = json.load(f)

                check = check_nominee(txt_data, election_id, voter_id)
                return Response({'success': check})
        else:
            f = open('voting/' + file_name, 'w+')
            f.write('[]')
            # txt_data = json.load(f)
            # check = check_nominee(txt_data,election_id,voter_id)
            return Response({'success': True})

    def post(self, request, election_id, voter_id, format=None):
        # nom_data = request.data
        if request.POST:
            myDict = dict(request.data)


            got_list = json.loads(next(iter(myDict.keys())))

            elect = dict(got_list[0])
            voter = dict(got_list[1])
            nom1 = dict(got_list[2])
            nom2 = dict(got_list[3])
            nom3 = dict(got_list[4])

            elec_id = elect["value"]
            voter_id = voter["value"]
            nom_data1 = [nom1["value"], nom1["name"]]
            nom_data2 = [nom2["value"], nom2["name"]]
            nom_data3 = [nom3["value"], nom3["name"]]
            nom_data_full = [nom_data1, nom_data2, nom_data3]


            blockchain.add_nom_block(elec_id, voter_id, nom_data_full)

        return Response({'success': True})

    

# to get the result of voted registered  user
class CheckVoter(APIView):


    def get(self, request, election_id, voter_id, format=None):
        input_data = request.data

        file_name = '' + election_id + '.json'

        if os.path.exists('voting/' + file_name):
            with open('voting/' + file_name, 'r') as f:
                print('voting/' + file_name)
                txt_data = json.load(f)

                check = check_voter(txt_data, election_id, voter_id)
                return Response({'success': check})
        else:
            f = open('voting/' + file_name, 'w+')
            f.write('[]')
            # txt_data = json.load(f)
            # check = check_nominee(txt_data,election_id,voter_id)
            return Response({'success': True})

    def post(self, request, election_id, voter_id, format=None):
        # nom_data = request.data
        if request.POST:
            myDict = dict(request.data)

            got_list = json.loads(next(iter(myDict.keys())))
            # print(len(got_list))

            elect = dict(got_list[0])
            voter = dict(got_list[1])
            nom1 = dict(got_list[2])
            nom2 = dict(got_list[3])
            nom3 = dict(got_list[4])

            elec_id = elect["value"]
            voter_id = voter["value"]
            nom_data1 = [nom1["value"], nom1["name"]]
            nom_data2 = [nom2["value"], nom2["name"]]
            nom_data3 = [nom3["value"], nom3["name"]]
            nom_data_full = [nom_data1, nom_data2, nom_data3]


            blockchain.add_vote_block(elec_id, voter_id, nom_data_full)

        return Response({'success': True})



# Check received json data
def json_check(request):
    with open('voting/data.json', 'r') as f:
        data = json.load(f)
        print(data)
    return HttpResponse("Checked")


# To send nominee result after voting
class GetNomResult(APIView):
    def get(self, request, elec_id, format=None):

        f = open('result.json', 'r')
        data = f.read()
        mydict = json.loads(data)
        f.close()

        print(mydict)

        return Response({'pres': mydict[elec_id][0], 'vp': mydict[elec_id][1], 'sec': mydict[elec_id][2]})


# To send voter results after voting
class GetVoterResult(APIView):
    def get(self, request, elec_id, format=None):
        # from golbal variable send data as JSON
        print(elec_id)

        f = open('result.json', 'r')
        data = f.read()
        mydict = json.loads(data)
        f.close()

        print(mydict)

        return Response({'pres_final_cnt': mydict[elec_id][3], 'vp_final_cnt': mydict[elec_id][4], 'sec_final_cnt': mydict[elec_id][5]})
