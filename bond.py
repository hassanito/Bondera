#fixed income securities
import math
import matplotlib
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

def main():
    #from Bond import *
    #from tkinter import *
    
    
    import matplotlib.pyplot as plt
    
    window = Tk()
    
    def bress():
        print(period.get())
        print(max_invest1.get())
        popo  = Simulation.initial_investment_variable_graph(int(period.get()),int(max_invest1.get()))
        plt.plot(popo[0],popo[1])
        plt.xlabel('initial investment')
        plt.ylabel('Profit')
        plt.show()
        
    def bress2():
        popo = Simulation.initial_period_variable_graph(int(initial_invest.get()),int(max_years.get()))
        plt.plot(popo[0],popo[1])
        plt.xlabel('initial investment period in years')
        plt.ylabel('Profit')
        #plt.axis([0,max_number_of_years,0,accounts[len(accounts)-1]])
        plt.show()
        
    def bress3():
        popo = Simulation.investment_3d_graph(int(initial_pe.get()),int(initial_in.get()),int(max_pe.get()),int(max_in.get()))
        ax=popo[0]
        ys=popo[1]
        zs=popo[3]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xs,ys,zs)
        ax.set_xlabel('initial investment')
        ax.set_ylabel('investment period')
        ax.set_zlabel('profit')
        plt.show()
        
        
    
    period = StringVar()
    max_invest1 =StringVar()
    
    initial_invest = StringVar()
    max_years = StringVar()
    
    initial_in = StringVar()
    initial_pe = StringVar()
    max_in = StringVar()
    max_pe = StringVar()
    
    two_d = Label(window,text = '2D',relief = 'raised')
    two_d.grid(column=0 , row=0, sticky =(W))
    
    frame1 = ttk.LabelFrame(window,text = 'the initial investment variable')
    frame1.grid(row=1,column=0,sticky = (W),padx=50,pady=50)
    
    ttk.Label(frame1, text = 'period of the investment').grid(row=2,column=0,padx=20)
    ttk.Entry(frame1,textvariable= period).grid(row=2,column=1,padx=20)
    ttk.Label(frame1,text= ' maximum investment').grid(row=3,column=0,padx=20)
    ttk.Entry(frame1,textvariable= max_invest1).grid(row=3,column=1,padx=20)
    ttk.Button(frame1,text='Simulate',command = bress).grid(row=4,column=0,padx=50)
    
    frame2 = ttk.LabelFrame(window,text = ' the initial period variable')
    frame2.grid(column=0,row=2,sticky = (W),padx=50,pady=50)
    ttk.Label(frame2, text = 'investment ammount').grid(row=2,column=0,padx=20)
    ttk.Entry(frame2,textvariable= initial_invest).grid(row=2,column=1,padx=20)
    ttk.Label(frame2,text= 'maximum period').grid(row=3,column=0,padx=20)
    ttk.Entry(frame2,textvariable= max_years).grid(row=3,column=1,padx=20)
    ttk.Button(frame2,text='Simulate',command = bress2).grid(row=4,column=0,padx=50)
    
    three_d = Label(window,text = '3D', relief = 'raised')
    three_d.grid(column=0,row=3,sticky = (W))
    
    frame3 = ttk.LabelFrame(window,text = 'initial investment and period variable')
    frame3.grid(column=0 ,row=4,sticky = (W),padx=50)
    
    ttk.Label(frame3,text = 'initial investment').grid(row=0,column=0,padx=20)
    ttk.Entry(frame3,textvariable = initial_in).grid(row=0,column=1,padx=20)
    
    ttk.Label(frame3,text = 'initial period').grid(row=1,column=0,padx=20)
    ttk.Entry(frame3,textvariable = initial_pe).grid(row=1,column=1,padx=20)
    
    
    ttk.Label(frame3,text = 'maximum investment').grid(row=2,column=0,padx=20)
    ttk.Entry(frame3,textvariable = max_in).grid(row=2,column=1,padx=20)
    
    
    ttk.Label(frame3,text = 'maximum period').grid(row=3,column=0,padx=20)
    ttk.Entry(frame3,textvariable = max_pe).grid(row=3,column=1,padx=20)
    ttk.Button(frame3,text='Simulate',command = bress3).grid(row=4,column=0,padx=50)
    
    
    
    
    
    
    window.mainloop()



class Bond:
    def __init__(self,price,maturity,interest,yield_period,risk):
        self.price = price
        #the price could be in any currency 
        self.maturity = maturity
        #the maturity is in years 
        self.interest = interest 
        #the interest or coupon is payed every yield period
        self.yield_period = yield_period
        self.risk = risk
        self.risk_factor = Bond.rating_to_risk_factor(self.risk)
        #self.yield_to_maturity = Bond.yield_to_maturity()
        
        
        self.period = 0
        #I used a number to store the term that returns the period 2 for twice in 1 year ,1 for once yearly and 12 for once a month 12 years a month
        if(self.yield_period == 'half'):
            self.period = 2
        elif(self.yield_period == 'yearly'):
            self.period = 1
        elif(self.yield_period == 'monthly'):
            self.period = 12
            
            
        
    def yield_to_maturity(self):
        ytm=0
        #this function calculates the yield when the bond matures
        for i in range(self.maturity):
            for i in range(self.period):
                ytm = ytm + self.interest*self.price 
        return ytm
     #this function provides the use with information about the bond   
    def get_info(self):
        print('the price of this bond is ' +str(self.price))
        print('this bond will reach maturity in ' + str(self.maturity)+ ' years' )
        print('this bond has an interest rate of '+str(self.interest*100) + '% that is paid '+ str(self.yield_period))
        print('this bond has a rating of '+ str(self.risk))
        print('this bond yield to maturity is ')
        print('-------------------------------------------------')
    
    def get_interest(self):
        return self.interest
        
        
    def rating_to_risk_factor(risk):
        #the higher the risk of the bond the higher the risk factor (a number would be)
        #the letters are credit ratings by credit ratings agencies (standard & poor)
        
        risk_factor=0
        if(risk == 'AAA'):
            risk_factor = 0
        elif(risk == 'AA+'):
            risk_factor = 1
        elif(risk == 'AA'):
            risk_factor = 2
        elif(risk == 'AA-'):
            risk_factor = 3
        elif(risk == 'A+'):
            risk_factor = 4
        elif(risk == 'A'):
            risk_factor = 5
        elif(risk == 'A-'):
            risk_factor = 6
        elif(risk == 'BBB+'):
           risk_factor = 7
        elif(risk == 'BBB'):
            risk_factor = 8
        elif(risk == 'BBB-'):
            risk_factor = 9
        elif(risk == 'BB+'):
            risk_factor = 10
        elif(risk == 'BB'):
            risk_factor = 11
        elif(risk == 'BB-'):
            risk_factor = 12
        elif(risk == 'B+'):
            risk_factor = 13
        elif(risk == 'B'):
            risk_factor = 14
        elif(risk == 'B-'):
            risk_factor = 15
        elif(risk == 'CCC+'):
            risk_factor = 16
        elif(risk == 'CCC'):
            risk_factor = 17
        elif(risk == 'CCC-'):
            risk_factor = 18
        elif(risk == 'CC'):
            risk_factor = 19
        elif(risk =='C'):
            risk_factor = 20
        elif(risk == 'D'):
            risk_factor = 21
        return risk_factor
        
        
        
    def bond_interest_to_rating(risk_factor):
        #this function takes the risk factor I created as an argument and returns an interest rate ,the higher risk the higher the interest rate will be
        counter = 0
        interest = random.randint((risk_factor-int(risk_factor*1/2))*10,(risk_factor+random.randint(1,5))*10)*0.001
        return interest
        
    
    def random_bond():
        #this function creates  a random bond with a random price,maturaty,interest,rating and yield period
        price = random.randint(600,1500)
        #print(price)
        maturity = random.randint(1,30)
        
        #this list contains 2 possible choices for a bond which are yearly of half and they will be chosen randomly by the index randomly created 
        possible_yield_period = ['half','yearly']
        yield_choice = random.randint(0,1)
        yield_period = possible_yield_period[yield_choice]
        possible_bond_rating = ['AAA','AA+','AA','AA-','A+','A','A-','BBB+','BBB','BBB-','BB+','BB','BB-','B+','B','B-','CCC+','CCC','CCC-','CC','C','D']
        bond_rating_choice = random.randint(0,21)
        bond_rating = possible_bond_rating[bond_rating_choice]
        interest = Bond.bond_interest_to_rating(Bond.rating_to_risk_factor(bond_rating))
        bond = Bond(price,maturity,interest,yield_period,bond_rating)
        #bond.get_info()
        
        return bond
    def random_bond_list():
        bond_market = []
        # I am creating a list that contains a random number of bonds with random price,interest rates,ratings and maturity
        number_of_bonds_in_market = random.randint(50000,100000)
        for i in range(number_of_bonds_in_market):
            bond_market.append(Bond.random_bond())
            
        return bond_market
        
    
        
        
        
class Simulation():
    
    def __init__(self,initial_investment,period):
        self.initial_investment = initial_investment
        self.period = period

    #the simulation class corresponds to a simulation of a one time investment created by the user that inherits the Bond class
    #the initial_investment is the principal sum the investor wishes to buy bonds with
    #the period is the time period which the user wants the return after it finishes
        #the year 
        self.year = period
        self.bonds_owned = []
        #self.bonds_owned_history=[]
        self.account = initial_investment
        self.number_of_bonds_owned =0
        
        
    def market_sorting_rating(bondmarket):
        sorted_market = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],15:[],14:[],16:[],17:[],18:[],19:[],20:[],21:[]}
        #the randomly generated market will be sorted in a dictionnary according to ratings
        for i in bondmarket:
            sorted_market[i.risk_factor].append(i)
        return sorted_market
        
    def market_sorting_interest(market):
        #takes a market list as an entry and returns a list sorted with the highest interest rates in the beginning 
        z=sorted(market, key=Bond.yield_to_maturity)
        z.reverse()
        return z
        
    def market_sorting_rating_and_interest(market_list):
        #this function takes a market list of random bonds and arranges them in a dictionnary according to risk factor and each list in each key is sorted according to the interest rate
        market_Dict = Simulation.market_sorting_rating(market_list)
        sorted_market = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],15:[],14:[],16:[],17:[],18:[],19:[],20:[]}
        for i in market_Dict.values():
            market = Simulation.market_sorting_interest(i)
            #print(market[0].risk_factor)
            sorted_market[market[0].risk_factor] = market
            
        return sorted_market
        
        
    def market_Dict_to_2D_list(market_dict):
        #this function takes a dictionary containing lists according to ranking and returns a 2 dimensional array
        market_list = list(market_dict.values())
        return market_list
        
    def delete_junk_bonds(market_list):
        #this function deletes all junk bonds (junks with a rating of BB or lower thus with a risk factor of 11 or bigger
        return market_list[0:11]
        
    
    def sorted_market(market):
        #this function takes the list of bonds in the market an returns a 2 dimensional list containg the bonds sorted according to their rating and interest rates
        market_Dict = Simulation.market_sorting_rating_and_interest(market)
        sorted_market_list = Simulation.market_Dict_to_2D_list(market_Dict)
        new_market = Simulation.delete_junk_bonds(sorted_market_list)
        return new_market
        
        
    def yearly_buy(self):
        #this function buys the best bonds in the market (randomly generated)after sorting the market according to interest and rating
        bond_market = Bond.random_bond_list()
        print(len(bond_market))
        sorted_market_list = Simulation.sorted_market(bond_market)
        #the first loop goes through the 11 ratings of bonds from the lowest risk to the highest
        for j in range(11):
            #the second loop buys the the bonds with the corresponding period
            for i in sorted_market_list[j]:
                if(i.maturity == self.year and self.account>=i.price and self.account>=0):
                    self.bonds_owned.append(i)
                    #self.bonds_owned_history.append(i)
                    self.number_of_bonds_owned +=1
                    self.account -= i.price
                    
            
    def bonds_owned_yearly_profit(self):
        #this function adds the yearly profit of every bond owned to the account of the investor
        for i in self.bonds_owned:
            self.account += i.price*i.interest
            i.maturity -= 1
        
    def bond_sell(self):
        #this function sells the bonds when it reaches maturity
        for i in self.bonds_owned:
            if(i.maturity ==0):
                self.account += i.price
                self.bonds_owned.remove(i)
    
    def bond_sell_before_maturity(self):
        #this function sells bonds before they reach maturity
        for i in self.bonds_owned:
            self.account += i.price
            self.bonds_owned.remove(i)
            #print(i)
            
    
    def year_update(self):
        #this function runs every year, updates the account with the profits from the bonds owned and reinvest the sum in the bond market
        #the first function adds to the account the profits
        self.bonds_owned_yearly_profit()
        #the second function sells the bonds that reached maturity
        self.bond_sell()
        #the third function reinvests the sum 
        self.yearly_buy()
                
                
                
    def total_simulation_buy(self):
        #the first loop keeps buying and selling bonds
        for i in range(self.period):
            self.year_update()
            self.year -=1
        for i in range(0,10):
            self.bond_sell_before_maturity()
        
            
            
    def main_simulation(initial_investment,investment_period):
        simulation = Simulation(initial_investment,investment_period)
        simulation.total_simulation_buy()
        print('we bought ' +str(simulation.number_of_bonds_owned))
        print('account'+str(simulation.account-initial_investment))
        return simulation.account-initial_investment
        
    def initial_period_variable_graph(initial_investment,max_number_of_years = 10):
        #the inital investment is a fixed ammount and the initial period of the investment is a varibale
        z=1
        accounts = []
        for i in range(max_number_of_years):
            accounts.append(Simulation.main_simulation(initial_investment,i))
        #plt.plot(range(max_number_of_years),accounts)
        #plt.xlabel('initial investment period in years')
        #plt.ylabel('Profit')
        #plt.axis([0,max_number_of_years,0,accounts[len(accounts)-1]])
        #plt.show()
        return (range(max_number_of_years),accounts)
    
    def thousand_list(number):
        #this is a function that takes a number and return a list containing the 1000 multiple of this 
        liste = []
        for i in range(number+1):
            liste.append(i*1000)
        del liste[0]
        return liste
        
    def initial_investment_variable_graph(initial_period,max_initial_investment=10000):
        #the initial period of investment is a fixed ammount and the initial investment is a variable
        z=Simulation.thousand_list(int(max_initial_investment/1000))
        accounts = []
        for i in z:
            accounts.append(Simulation.main_simulation(i,initial_period))
        #plt.plot(z,accounts)
        #plt.xlabel('initial investment')
        #plt.ylabel('Profit')
        #plt.show()
        return (z,accounts)
                
    def investment_3d_graph(initial_period,inital_investment,max_period=10,max_investment=5000):
        accounts =[]
        investment_list=Simulation.thousand_list(int(max_investment/1000))
        print(investment_list)
        xs=[]
        ys=[]
        zs=[]
        for i in investment_list:
            for j in range(max_period):
                accounts.append(Simulation.main_simulation(i,j))
                xs.append(i)
                ys.append(j)
        zs = accounts
        return (xs,ys,zs)
        #print(len(xs))
        #print(len(ys))
        '''fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
       
        ax.scatter(xs,ys,zs)
    
        ax.set_xlabel('initial investment')
        ax.set_ylabel('investment period')
        ax.set_zlabel('profit')
    
        plt.show()'''
    
