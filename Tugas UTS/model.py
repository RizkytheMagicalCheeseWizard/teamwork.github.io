from metaflow import FlowSpec, step

class PerkuliahanFlow(FlowSpec):
    @step
    def start(self):
        print("Start College Process")
        self.next(self.spp_payment)
    @step
    def spp_payment(self):
        self.spp_payed = True
        if self.spp_payed:
            print("Already payed")
        else:
            print("Not yet")
        self.next(self.confirm_payment)
    @step
    def confirm_payment(self):
        if self.spp_payed:
            print("SPP payment has been confirmed")
            
        else:
            print("SPP payment hasn't been confirmed")
            self.next(self.end)
        self.next(self.attend_class)
    @step
    def attend_class(self):
        print("Attend classes and lectures directly")
        self.total_attend = 14
        self.presence = 0

        for i in range(1,self.total_attend + 1):
            attend = True
            if attend:
                self.presence += 1
            print(f"day {i}: {'attend' if attend else 'Not attend'}")
        self.min_attend = int(0.75 * self.total_attend)
        if self.presence>=self.min_attend:
            print("Meet attendance requirements")
        else:
            print("Not meet attendance requirment")
            self.next(self.end)
        self.next(self.attend_uts)
    @step
    def attend_uts(self):
        score = 80
        self.uts_score = score
        print(f"UTS Score : {self.uts_score}")
        self.next(self.attend_uas)
    @step
    def attend_uas(self):
        score = 90
        self.uas_score = score
        print(f"UAS Score : {self.uas_score}")
        self.next(self.calculate_final_score)
    @step
    def calculate_final_score(self):
        self.final_score = (self.uts_score + self.uas_score)/2
        print(f"Final Score : {self.final_score}")
        self.next(self.end)
    @step
    def end(self):
        print('Done')
if __name__ == '__main__':
    PerkuliahanFlow()
        
        
