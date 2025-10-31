# src/recommendations.py

def get_recommendations(risks, inputs):
    recs = []
    
    if risks['diabetes'] > 60:
        recs.append("Reduce sugar & refined carbs")
        recs.append("Walk 30 min daily")
        if inputs['BMI'] > 30:
            recs.append("Aim to lose 5-7% body weight")
    
    if risks['heart_disease'] > 60:
        recs.append("Limit salt <2g/day")
        recs.append("Eat oats, nuts, and olive oil")
        if inputs['Smoking'] == 1:
            recs.append("Quit smoking immediately")
    
    if risks['stroke'] > 60:
        recs.append("Control blood pressure daily")
        recs.append("Manage stress with meditation")
    
    return recs[:3]