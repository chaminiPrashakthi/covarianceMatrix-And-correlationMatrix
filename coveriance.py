import numpy as np
import pandas as pd
import statistics as st

df = pd.read_csv('coveriance.csv')
df.shape
N=len(df[:])
mean = df.mean()
df.fillna(mean,inplace=True)
	
class cov:

	def covariance(self,x,y):
		sum =0
		mean_x= np.mean(x)
		mean_y= np.mean(y)
		#print mean_x
		N= len(x)
		for j in range(0,N):
			val_X= x[j]-mean_x
			val_Y= y[j]-mean_y
			mult = val_X * val_Y
			sum += mult
		final = sum/ (N-1)
		#print final
		return final
		
	def variance(self,x):
		N=len(x)
		sd_X =0
		mean_x= np.mean(x)
		for j in range(0,N):
			val_X1= x[j]-mean_x
			squre_X = val_X1**2
			sd_X +=squre_X
		variance = sd_X/(N-1)
		return variance
		
	def correlation(self,x,y):
			var_cor= self.covariance(x,y)/(np.sqrt(self.variance(x)*self.variance(y)))
			return var_cor
		
	
	
	
object=cov()
covariance_Matrix=  np.zeros((5,5),dtype=np.float)
correlation_Matrix=  np.zeros((5,5),dtype=np.float)		
for i in range (0,5):
	for j in range (0,5):
		x= df.iloc[:,i]
		y= df.iloc[:,j]
		correlation_Matrix[i,j]= object.correlation(x,y)
		if i==j:
			covariance_Matrix[i,j]= object.variance(x)
		else:
			covariance_Matrix[i,j]= object.covariance(x,y)
print "-----------------------------------------------"
print "Covariance Matrix"
print covariance_Matrix
print "-----------------------------------------------"

print "correlation Matrix"
print correlation_Matrix
print "-----------------------------------------------"

#Test cases
import unittest


class Test(unittest.TestCase):
	object=cov()
	
	A1 = [1,3,1,1,1]
	A2 = [2,2,1,2,2]
	A3 = [3,4,1,12,23]

	def setUp(self):
		print("set up")
	
	def test_find_variance(self):
		test1 = self.object.variance(self.A1)
		self.assertTrue((st.variance(self.A1)-test1)<=0.0001,msg="Invalid Output")
		
	def test_find_covariance(self):
		test2 = self.object.covariance(self.A1,self.A2)
		self.assertEquals(0.1,test2,msg="Invalid Output")
		
	def test_find_correlation(self):
		test3 = self.object.correlation(self.A1,self.A2)
		self.assertTrue((test3-0.25)<=0.00000001,msg="Invalid Output")
	
	def tearDown(self):
		print("tear down")
		
	
if __name__== '__main__':
	unittest.main()	
