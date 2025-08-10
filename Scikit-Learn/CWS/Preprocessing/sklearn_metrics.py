from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [1, 0, 1, 1, 0, 1, 0]

y_pred = [1, 0, 1, 0, 0, 1, 1]

print('Acuracy : ', accuracy_score(y_true, y_pred))
print('Precision : ', precision_score(y_true, y_pred))
print('Recallscore : ', recall_score(y_true, y_pred))
print('F1score : ', f1_score(y_true, y_pred))

from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

real_score = [90, 60, 80, 100]

pred_score = [85, 70, 70, 95]

mae = mean_absolute_error(real_score, pred_score)

mse = mean_squared_error(real_score, pred_score)

rmse = root_mean_squared_error(real_score, pred_score)

print('mean_absolute_error : ',mae)
print('mean_squared_error : ',mse)
print('root_mean_squared_error : ',rmse)