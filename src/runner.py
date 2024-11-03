from model_service import ModelService

def main():
    ml_svc = ModelService()
    ml_svc.load_model('rf_v1')
    pred = ml_svc.predict([[100, 3, 2, 2, 1, 1, 1, 1, 1, 1]])
    print(f'Predicted rent: {pred[0]}')

if __name__ == '__main__':
    main()