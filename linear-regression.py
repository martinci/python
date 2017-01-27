# Program: Linear Regression from scratch.

def dot_prod(a1, a2, n):
    # given 2 arrays of same size n we compute their std euclidean dot product
    return sum([a1[i]*a2[i] for i in range(n)])
    
def mean(a):
    return sum(a)/len(a)

def std(a):
    m = mean(a)
    return (sum([(x - m)**2 for x in a])/len(a))**0.5
    
def normalize_data(X):
    X_new = []
    features = [[X[j][i] for j in range(n)] for i in range(p)]
    m = []
    s = []
    
    for i in range(len(X[0])):
        m.append(mean(features[i]))
        s.append(std(features[i]))
    
    for i in range(len(X)):
        new_obs = [(X[i][j] - m[j])/s[j] for j in range(len(X[0]))]
        X_new.append(new_obs)
        
    return [X_new, m, s]

def transform(X,m,s):
    X_new = []
    for i in range(len(X)):
        new_obs = [(X[i][j] - m[j])/s[j] for j in range(len(X[0]))]
        X_new.append(new_obs)
    return X_new
    
class LinearRegression:
    #before making predictions we need to train first
    is_trained = False
    #number of features
    p = 0
    #number of observations in the training data
    n = 0
    trainError = []
        
    def __init__(self, max_iter, alpha = 0.1):
        # X is the training data, Y is the trainning target, b are the weights
        self.max_iter = max_iter
        #step size for gradient descent
        self.alpha = alpha
        self.X = []
        self.Y = []
        self.b = []
        
    def rss(self):
        if self.is_trained:
            return sum([(self.Y[i] - dot_prod(self.b,[1] + self.X[i],p+1))**2 for i in range(n)])/n
        else:
            print('You need to train me for this...')
            
    def fit(self, Y, X, display_error = False):
        self.n = len(X)
        self.p = len(X[0])
        self.X = X
        self.Y = Y
        #self.b = [sum(Y)/n] + p*[0]
        self.b = (p+1)*[0]
        self.is_trained = True
        
        # We use gradient descent to minimize the RSS
        for _ in range(self.max_iter):
            rss_aux = [-(self.Y[i] - dot_prod(self.b, [1] + self.X[i], p+1))/n for i in range(n)]
            #print('rss_aux = {}'.format(rss_aux))
            features = [[self.X[j][i] for j in range(n)] for i in range(p)]
            #print('features[0] = ',features[0])
            grad_rss = [sum(rss_aux)] + [dot_prod(rss_aux,features[i],n) for i in range(p)]
            # update weights in the direction of the gradient of rss
            self.b = [self.b[i] - self.alpha*grad_rss[i] for i in range(p+1)]
            # keep track of the errors
            current_error = self.rss()
            self.trainError.append(current_error)
        if display_error:
            print(self.trainError)
    
    def predict(self,X):
        if self.is_trained:
            return [dot_prod(self.b,[1] + X[i],p+1) for i in range(p)]
        else:
            print('You need to train me for this...')

        
if __name__ == '__main__':
    X = []
    Y = []
    p = 1 # only one feature in this case
    n = 5 # we have 5 observations
    for _ in range(n):
        # A general line in 2D is y = b_0 + b_1 x. 
        # We find b_i by minimizing \sum_{i=1}^n (y_i - \hat y_i)^2,
        # where n is number of observations
        # and \hat y_i = b_0 + b_1 x_i is the predicted value
        x,y = map(int, input().strip().split())
        X.append([x])
        Y.append(y)
    X, m, s = normalize_data(X)
    lm = LinearRegression(1000, alpha=0.1)
    lm.fit(Y,X)
    X_pred = [[80]]
    X_pred = transform(X_pred,m,s)
    Y_pred = lm.predict(X_pred)
    for y_pred in Y_pred:
        print('{:.3f}'.format(y_pred))
        
