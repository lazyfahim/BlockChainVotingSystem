import hashlib
import json


class BlockChain:
    previousHash = None
    pres = []
    vp = []
    sec = []

    def __init__(self):
        self.previousHash = None
        self.pres = []
        self.vp = []
        self.sec = []

    def hash_block(self, electionID, voterID, block_type, data):
        """
        Send the data received from the post request into this function to generate a JSON file
        which will be saved to a file. This function will perform the hashing required for block chain.
        """
        vote_data = {
            "elec_id": electionID,
            "voter_id": voterID,
            "block_type": block_type,
            block_type+"_data": data,
            "prev_hash": self.previousHash
        }

        vote_serialized = json.dumps(vote_data).encode('utf-8')
        vote_hashed = hashlib.sha256(vote_serialized).hexdigest()
        self.previousHash = vote_hashed
        return vote_serialized

    def add_vote_block(self, elec_id, voter_id, vote_data):
        hash_data = self.hash_block(elec_id, voter_id, "vote", vote_data).decode("utf-8")
        hash_data_json = json.loads(hash_data)

        file = open('vote.json', 'r')
        file_data = file.read()
        file_data_json = json.loads(file_data)
        file.close()

        data = file_data_json + [hash_data_json]
        file = open('vote.json', 'w')
        file.write(json.dumps(data))
        file.close()

        file = open('vote.json', 'r')
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

    # def check_hash_codes(self, blocks, next_block):
    #     """
    #     This function will check if the previous block was tampared or not by checking it's hash with that stored in
    #     the next block.
    #     """
    #     error = False

    #     for i in range([::-1]):
    #         vote_hashed = hashlib.sha256(blocks[i].encode('utf-8')).hexdigest()

    
blockchain = BlockChain()
blockchain.add_vote_block("1", "2", [("205", "pres"), ("25525", "vice"), ("554", "sec")])
blockchain.add_vote_block("1", "3", [("215", "pres"), ("55525", "vice"), ("553", "sec")])
blockchain.add_vote_block("1", "4", [("202", "pres"), ("6525", "vice"), ("518", "sec")])
blockchain.add_vote_block("1", "5", [("203", "pres"), ("75525", "vice"), ("158", "sec")])
blockchain.add_vote_block("1", "6", [("245", "pres"), ("27525", "vice"), ("568", "sec")])
