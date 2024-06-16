import streamlit as st


st.set_page_config(page_title="Diabetes Analysis Dashboard", layout="wide")
st.sidebar.title("Navigation")
sidebar_choice = st.sidebar.radio('Select Analysis', ['Dashboard', 'BMI Calculator', 'Exercise Routine Generator', 'Medication Management', 'Exercises and Eating Healthy', 'Mindfulness and Stress Management', 'Smoking Risks', 'Cholesterol', 'High Blood Pressure', 'Initiatives', 'Success Stories', 'Recommendations'])

if sidebar_choice == 'Dashboard':
st.subheader('Interactive Tableau Dashboard')
# Embed Tableau dashboard using an iframe
tableau_embed_code = """
<iframe src='https://public.tableau.com/views/Healthcareanalytics-cjk08/DiabetesDashboard-cjk08?:embed=y&:showVizHome=no' width='1300' height='1363' frameborder='0'></iframe>
"""
st.markdown(tableau_embed_code, unsafe_allow_html=True)\

st.markdown("""
The Diabetes Analysis Dashboard provides a comprehensive visualization of diabetes distribution across different age groups and sexes. It offers insights into how diabetes prevalence varies among young adults (18-39 years), middle-aged adults (40-59 years), and older adults (60+ years). The dashboard highlights the following key areas:

1. **Distribution of Survey Participants Across Different Age Groups and Sexes (%)**: This bar chart visualizes the distribution of survey participants across various age groups, segmented by sex. It reveals the demographic spread of the participants, highlighting a significant representation in the 65-69 age group. This data helps in understanding the demographic composition of the survey respondents, which is crucial for ensuring the accuracy and relevance of public health interventions.

2. **Diabetic vs Non-Diabetic Percentage by Age Group**:
    - **Young Adults (18-39 years)**: A pie chart illustrating the proportion of young adults who are diabetic versus non-diabetic.
    - **Middle-Aged Adults (40-59 years)**: A pie chart showing the diabetic versus non-diabetic distribution in middle-aged adults.
    - **Older Adults (60+ years)**: A pie chart depicting the diabetic versus non-diabetic percentage among older adults.

3. **Prevalence of Diabetes by General Health Status**: A horizontal bar chart that shows how diabetes prevalence varies with different general health statuses (Excellent, Very Good, Good, Fair, Poor).

4. **Distribution of General Health Status Among Diabetic Individuals**: A pie chart that provides a breakdown of the general health status among those who are diabetic.

5. **Average BMI for Diabetic vs Non-Diabetic Individuals**: A table comparing the average BMI of diabetic and non-diabetic individuals, highlighting that those with diabetes tend to have a higher BMI.

6. **Age Group Distribution of Obese Diabetic Individuals (BMI > 30)**: A tree map illustrating the distribution of obese individuals with diabetes across different age groups.

7. **Cholesterol Check with Diabetes Status**: A pie chart showing the percentage of individuals who have checked their cholesterol levels, segmented by diabetic and non-diabetic status.

8. **Prevalence of High Blood Pressure Among Diabetic/Non-Diabetic Individuals**: A pie chart that highlights the prevalence of high blood pressure among diabetic and non-diabetic individuals.

9. **Prevalence of Diabetes Among Smokers and Non-Smokers**: Pie charts comparing the prevalence of diabetes among smokers versus non-smokers.

These visualizations provide critical insights into the demographic and health-related factors associated with diabetes. The dashboard is designed to help identify patterns and inform strategies for diabetes prevention and management.
""")
elif sidebar_choice == 'Recommendations':
st.subheader('Comprehensive Health Recommendations')


# Flash the user with engaging information about overall health recommendations
st.markdown("""
### 🏥 Comprehensive Health Recommendations
Achieving and maintaining good health requires a holistic approach that includes managing your BMI, quitting smoking, staying physically active, eating a healthy diet, controlling cholesterol, and managing high blood pressure. Here’s a comprehensive guide to help you achieve your health goals:

![Healthy Lifestyle](https://www.cdc.gov/chronicdisease/resources/infographic/preventable/power-of-prevention.jpg)

### 🏋️‍♂️ Maintain a Healthy BMI

**1. Calculate Your BMI:**
- Regularly check your BMI to ensure you are within a healthy range. A healthy BMI is between 18.5 and 24.9.

**2. Manage Your Weight:**
- If your BMI is outside the healthy range, focus on weight management strategies through a balanced diet and regular exercise.

![BMI Categories](https://www.cdc.gov/healthyweight/images/assessing/bmi-adult-fb-600x315.png)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**: 
    - Develop community programs that promote regular BMI screenings and provide resources for weight management.
    - Implement public health campaigns that emphasize the importance of maintaining a healthy BMI.
    - Partner with local organizations to create support groups for weight management.
- **Healthcare Providers**: 
    - Educate patients on the importance of maintaining a healthy BMI and provide personalized weight management plans.
    - Offer regular BMI checks during routine visits and track progress over time.
    - Provide referrals to nutritionists and dietitians for specialized support.
- **Policymakers**: 
    - Support policies that increase access to healthy foods and safe places for physical activity.
    - Advocate for school programs that promote physical education and healthy eating habits.
    - Fund initiatives that address food deserts and improve community access to nutritious foods.

### 🚭 Quit Smoking

**1. Understand the Risks:**
- Smoking increases the risk of numerous health issues, including heart disease, stroke, respiratory problems, and diabetes.

**2. Strategies to Quit:**
- Set a quit date, inform family and friends, anticipate challenges, remove tobacco products, and seek medical advice.

**3. Healthy Alternatives:**
- Replace smoking with healthy habits such as exercise, chewing gum, or deep breathing exercises.

![Smoking Risks](https://www.cdc.gov/tobacco/basic_information/health_effects/images/health-effects-infographic-600px.png)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**: 
    - Launch anti-smoking campaigns and provide resources for smoking cessation programs.
    - Offer free or subsidized smoking cessation programs and support groups.
    - Implement smoke-free policies in public areas and workplaces.
- **Healthcare Providers**: 
    - Offer smoking cessation support and resources during patient visits.
    - Prescribe smoking cessation aids such as nicotine patches or medications.
    - Follow up with patients regularly to track their progress and provide ongoing support.
- **Policymakers**: 
    - Implement and enforce policies that restrict tobacco advertising and increase taxes on tobacco products to reduce smoking rates.
    - Fund research on smoking cessation and its impact on public health.
    - Support legislation that bans smoking in public places and provides resources for smokers who want to quit.

### 🥗 Exercise and Eat Healthy

**1. Regular Physical Activity:**
- Engage in at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, along with strength training exercises twice a week.

**2. Balanced Diet:**
- Eat a variety of nutrient-rich foods, including fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods, sugars, and unhealthy fats.

![Exercise and Healthy Eating](https://www.verywellfit.com/thmb/7m1A9Z6SY_hR8nkp2gBPTrdJdug=/fit-in/1500x1250/filters:no_upscale():max_bytes(150000):strip_icc()/fitness-weightloss-5793d03c3df78c3276e2b45d.jpg)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**: 
    - Promote physical activity through community events and accessible public spaces.
    - Develop educational campaigns that emphasize the importance of a balanced diet and regular exercise.
    - Partner with schools and workplaces to implement wellness programs.
- **Healthcare Providers**: 
    - Encourage patients to incorporate regular exercise and balanced diets into their daily routines.
    - Provide resources and referrals to nutritionists and fitness experts.
    - Monitor patients' progress and adjust recommendations as needed.
- **Policymakers**: 
    - Support policies that ensure healthy food options are available and affordable.
    - Create safe environments for physical activity, such as parks and recreational facilities.
    - Fund programs that provide nutritional education and fitness classes to underserved communities.

### 🩺 Manage Cholesterol

**1. Eat Heart-Healthy Foods:**
- Reduce intake of saturated and trans fats, increase omega-3 fatty acids, and eat more soluble fiber.

**2. Regular Exercise:**
- Incorporate aerobic and strength training exercises to help manage cholesterol levels.

**3. Medication and Monitoring:**
- Follow medical advice for cholesterol-lowering medications and regularly monitor your cholesterol levels.

![Cholesterol](https://www.cdc.gov/cholesterol/images/what-is-cholesterol-800.jpg)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**: 
    - Raise awareness about the importance of cholesterol management through educational campaigns.
    - Provide community screening programs for cholesterol levels.
    - Offer workshops and resources on heart-healthy diets and lifestyles.
- **Healthcare Providers**: 
    - Monitor patients' cholesterol levels and provide guidance on maintaining heart-healthy lifestyles.
    - Prescribe medications and offer dietary recommendations to manage cholesterol.
    - Educate patients on the risks associated with high cholesterol and how to mitigate them.
- **Policymakers**: 
    - Advocate for policies that limit trans fats in foods and promote heart-healthy dietary options.
    - Fund public health initiatives that support cholesterol management programs.
    - Ensure that health insurance plans cover cholesterol screenings and management.

### 💓 Control High Blood Pressure

**1. Healthy Diet:**
- Reduce sodium intake, eat potassium-rich foods, and follow the DASH diet to manage blood pressure.

**2. Regular Physical Activity:**
- Engage in regular exercise to help lower and manage blood pressure.

**3. Stress Management:**
- Practice relaxation techniques, get enough sleep, and manage stress through healthy activities.

**4. Medication and Monitoring:**
- Adhere to prescribed medications for high blood pressure and regularly check your blood pressure.

![High Blood Pressure](https://www.cdc.gov/bloodpressure/images/BloodPressure_Infographic.jpg)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**: 
    - Implement community screening programs for blood pressure and educate the public about hypertension.
    - Provide resources and support for lifestyle changes that help manage blood pressure.
    - Launch public awareness campaigns on the importance of regular blood pressure monitoring.
- **Healthcare Providers**: 
    - Provide comprehensive management plans for patients with high blood pressure, including lifestyle modifications and medications.
    - Monitor patients' blood pressure regularly and adjust treatment plans as needed.
    - Educate patients on the risks of uncontrolled blood pressure and how to manage it effectively.
    - **Policymakers**:
    - Support legislation that promotes heart-healthy environments, such as reducing sodium in processed foods and ensuring access to affordable fresh produce.
    - Ensure that blood pressure screening and management programs are funded and accessible.
    - Advocate for workplace wellness programs that include blood pressure monitoring and stress management.

### 🌟 Holistic Health Approach

**1. Integrate Healthy Habits:**
- Combine these recommendations into your daily routine for a holistic approach to health. Regular check-ups with healthcare providers can help you stay on track.

**2. Stay Informed and Motivated:**
- Keep yourself educated about health risks and benefits. Use apps, support groups, and professional guidance to stay motivated.

**3. Make Incremental Changes:**
- Small, consistent changes can lead to significant health improvements. Start with manageable goals and gradually build healthier habits.

![Holistic Health](https://www.cdc.gov/chronicdisease/images/infographics/healthy-lifestyle.png)

**Recommendations for Public Health Officials, Healthcare Providers, and Policymakers:**
- **Public Health Officials**:
    - Promote a holistic approach to health through community programs and public awareness campaigns.
    - Develop initiatives that address multiple aspects of health and wellness simultaneously.
    - Partner with local organizations to create comprehensive health resources for the community.
- **Healthcare Providers**:
    - Encourage patients to adopt multiple healthy habits and provide support for making incremental changes.
    - Integrate holistic health approaches into patient care plans.
    - Offer resources and referrals to specialists in nutrition, exercise, mental health, and stress management.
- **Policymakers**:
    - Advocate for comprehensive health policies that address multiple aspects of health and wellness.
    - Ensure resources and support are available for holistic health programs in communities.
    - Fund research and programs that explore the benefits of holistic health approaches.

### 📝 Conclusion
Your health is your most valuable asset. By understanding and managing your BMI, quitting smoking, staying physically active, eating a balanced diet, controlling cholesterol, and managing high blood pressure, you can significantly improve your overall health and quality of life. Start today, take small steps, and stay committed to a healthier you.

![Healthy Lifestyle Conclusion](https://www.cdc.gov/chronicdisease/images/infographics/health-impact-infographic-600px.jpg)
""")
elif sidebar_choice == 'BMI Calculator':
st.subheader('BMI Calculator')


# Flash the user with interesting information about BMI
st.markdown("""
### Understanding Your BMI
**Body Mass Index (BMI)** is a simple calculation using a person's height and weight. It's an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity. Here's why BMI matters:

- **Indicator of Health**: A high BMI can be an indicator of high body fatness.
- **Predictor of Disease Risk**: BMI is used to screen for weight categories that may lead to health problems, such as heart disease, diabetes, and hypertension.
- **Simple and Accessible**: Calculating BMI is straightforward and can be done with basic information about your height and weight.

![BMI Categories](https://www.cdc.gov/healthyweight/images/assessing/bmi-adult-fb-600x315.png)

**Calculate your BMI below to find out your weight category and get personalized health advice.**
""")

# BMI Calculator
height = st.number_input('Enter your height (in cm):', min_value=50, max_value=300)
weight = st.number_input('Enter your weight (in kg):', min_value=10, max_value=500)

if height and weight:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f'Your BMI is: {bmi:.2f}')
    
    # Provide relevant suggestions based on BMI result
    if bmi < 18.5:
        st.markdown("""
        ### You are underweight.
        - **Nutrient-Rich Diet**: Include nutrient-rich foods in your diet to gain healthy weight.
        - **Frequent Meals**: Eat more frequently and choose high-calorie, nutrient-dense snacks.
        - **Consult a Professional**: Seek advice from a healthcare provider or a nutritionist to develop a balanced meal plan.

        **Note**: Being underweight can lead to health issues such as weakened immunity and osteoporosis. 
        """)
    elif 18.5 <= bmi < 24.9:
        st.markdown("""
        ### You have a normal weight.
        - **Maintain a Balanced Diet**: Continue eating a variety of foods to ensure you get all necessary nutrients.
        - **Stay Active**: Engage in regular physical activity to maintain your weight and improve overall health.
        - **Regular Check-Ups**: Schedule routine health check-ups to monitor your health status.

        **Great Job!**: Keeping a normal weight reduces the risk of chronic diseases.
        """)
    elif 25 <= bmi < 29.9:
        st.markdown("""
        ### You are overweight.
        - **Healthy Eating**: Focus on a diet rich in fruits, vegetables, whole grains, and lean proteins.
        - **Increase Physical Activity**: Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week.
        - **Behavioral Changes**: Consider behavioral strategies like mindful eating to prevent overeating.

        **Note**: Being overweight increases the risk of cardiovascular diseases and diabetes. 
        """)
    else:
        st.markdown("""
        ### You are obese.
        - **Balanced Diet**: Opt for a balanced diet low in processed foods, sugar, and unhealthy fats.
        - **Regular Exercise**: Engage in regular physical activity to help manage your weight.
        - **Seek Support**: Work with a healthcare provider to develop a weight-loss plan tailored to your needs.

        **Important**: Obesity significantly raises the risk of diabetes, heart disease, and other health conditions. Take proactive steps towards a healthier lifestyle.
        """)
        st.markdown("""
        **Advice**: Eating a balanced diet and staying active can significantly reduce your risk of diabetes and improve your overall health. Consider consulting a nutritionist and a fitness trainer to help you achieve your goals.
        """)
elif sidebar_choice == 'Smoking Risks':
st.subheader('Smoking Risks')


# Flash the user with engaging information about smoking risks
st.markdown("""
### 🚭 The Hidden Dangers of Smoking
Smoking is one of the leading causes of preventable deaths worldwide. It affects nearly every organ in the body, leading to a variety of health issues and chronic diseases. Here’s why smoking is hazardous:

![Smoking Risks](https://www.cdc.gov/tobacco/basic_information/health_effects/images/health-effects-infographic-600px.png)

**Health Risks of Smoking:**
- **Cardiovascular Disease**: Smoking damages blood vessels, leading to heart disease, stroke, and peripheral artery disease.
- **Respiratory Issues**: Chronic obstructive pulmonary disease (COPD), chronic bronchitis, and emphysema are common among smokers.
- **Cancer**: Smoking is linked to cancers of the lung, mouth, throat, esophagus, pancreas, bladder, and more.
- **Diabetes**: Smokers are 30-40% more likely to develop type 2 diabetes.
- **Weakened Immune System**: Smoking weakens the immune system, making the body more susceptible to infections.

![Health Risks](https://www.verywellhealth.com/thmb/Og3bJW2AX_P4_C5ktMzZOSX7jyk=/1333x1000/smart/filters:no_upscale()/gettyimages-531334777-5c629f6fc9e77c000146e100.jpg)

**Immediate and Long-term Benefits of Quitting Smoking:**
- **Within 20 Minutes**: Heart rate and blood pressure drop.
- **Within 12 Hours**: Carbon monoxide levels in the blood drop to normal.
- **Within 2-12 Weeks**: Circulation improves, and lung function increases.
- **Within 1-9 Months**: Coughing and shortness of breath decrease.
- **Within 1 Year**: Risk of coronary heart disease is half that of a smoker’s.
- **Within 5 Years**: Risk of stroke is reduced to that of a non-smoker.
- **Within 10 Years**: Risk of lung cancer falls to about half that of a smoker. Risk of other cancers decreases.
- **Within 15 Years**: Risk of coronary heart disease is that of a non-smoker’s.

![Benefits of Quitting Smoking](https://www.cancer.org/content/dam/cancer-org/images/infographics/quit-smoking-benefits-infographic.jpg)

### 🛑 Strategies to Quit Smoking

**1. Set a Quit Date:**
- Choose a date within the next two weeks to quit smoking. This gives you enough time to prepare but not too much time to change your mind.

**2. Inform Family and Friends:**
- Tell your family, friends, and colleagues about your plan to quit. Their support can make a significant difference.

**3. Anticipate and Plan for Challenges:**
- The urge to smoke is strong during the first few weeks after quitting. Plan for challenges and know how to handle cravings.

**4. Remove Cigarettes and Other Tobacco Products:**
- Get rid of cigarettes, lighters, ashtrays, and any other tobacco products from your home, car, and workplace.

**5. Talk to Your Doctor:**
- Discuss with your healthcare provider about your intention to quit. They can offer support, medications, and resources to help you.

![Strategies to Quit Smoking](https://www.quit.org.au/images/default-source/why-quit/quit-strategy.jpg)

### 🔄 Behavioral Strategies

**1. Avoid Triggers:**
- Identify situations that make you want to smoke and avoid them. This might include being around other smokers or places where you used to smoke.

**2. Manage Stress:**
- Find new ways to handle stress. Exercise, meditation, deep breathing, and hobbies can help reduce stress without smoking.

**3. Use Nicotine Replacement Therapy (NRT):**
- NRT can help reduce withdrawal symptoms. Options include nicotine patches, gum, lozenges, inhalers, and nasal sprays.

**4. Medication:**
- Prescription medications like Bupropion (Zyban) and Varenicline (Chantix) can help reduce cravings and withdrawal symptoms.

**5. Join a Support Group:**
- Support groups can provide encouragement and understanding. They offer a platform to share experiences and strategies.

### 🌟 Healthy Alternatives to Smoking

**1. Exercise:**
- Physical activity can help distract you from smoking and reduce cravings. It also helps manage weight gain and improves mood.

**2. Chewing Gum or Eating Healthy Snacks:**
- Keep your mouth busy with sugar-free gum or healthy snacks like fruits and vegetables.

**3. Deep Breathing Exercises:**
- Practice deep breathing exercises to relax and reduce the urge to smoke.

![Healthy Alternatives](https://www.verywellmind.com/thmb/PwX1a49Si17iW2EZdYFzL1nH5-8=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-507703741-56b5f17b3df78c0b136c89e3.jpg)

### 📞 Resources and Support

**1. Quitlines:**
- Many countries offer free telephone quitlines staffed by trained counselors. They can provide support and strategies for quitting.

**2. Mobile Apps:**
- There are numerous apps designed to help people quit smoking by tracking progress, providing motivational messages, and offering tips.

**3. Online Communities:**
- Join online forums and social media groups where you can connect with others who are trying to quit smoking.

### 🧠 What to Expect When You Quit

**Withdrawal Symptoms:**
- Expect some withdrawal symptoms as your body adjusts to being nicotine-free. These may include irritability, anxiety, difficulty concentrating, and increased appetite.

**Cravings:**
- Cravings are intense during the first few days but will gradually decrease. They typically last only a few minutes—find ways to distract yourself during this time.

**Mood Swings:**
- You might experience mood swings and irritability. This is normal and temporary as your body adapts.

**Weight Gain:**
- Some people gain weight when they quit smoking. Focus on eating healthy and staying active to manage weight.

**Improved Health:**
- Over time, you will notice significant improvements in your health. Breathing will become easier, your senses of taste and smell will improve, and your risk of smoking-related diseases will decrease.

![What to Expect](https://www.cdc.gov/tobacco/basic_information/quit_smoking/images/graphic/quit-smoking-tips-poster.jpg)

### 💡 Conclusion
Quitting smoking is challenging but incredibly rewarding. By understanding the risks, preparing strategies, and seeking support, you can successfully quit and enjoy a healthier, smoke-free life. Take the first step today towards a healthier future.
""")
elif sidebar_choice == 'Exercises and Eating Healthy':
st.subheader('Exercises and Eating Healthy')


# Flash the user with engaging information about the importance of exercise and healthy eating
st.markdown("""
### 🏋️‍♂️ The Power of Exercise and Healthy Eating
Regular physical activity and a balanced diet are cornerstones of a healthy lifestyle. They not only help in maintaining a healthy weight but also reduce the risk of chronic diseases such as diabetes, heart disease, and stroke. Here’s why exercise and healthy eating are essential:

![Healthy Lifestyle](https://www.verywellfit.com/thmb/7m1A9Z6SY_hR8nkp2gBPTrdJdug=/fit-in/1500x1250/filters:no_upscale():max_bytes(150000):strip_icc()/fitness-weightloss-5793d03c3df78c3276e2b45d.jpg)

**Benefits of Regular Exercise:**
- **Weight Control**: Exercise helps prevent excess weight gain and maintain weight loss.
- **Combats Health Conditions and Diseases**: Regular physical activity helps prevent or manage various health conditions, including stroke, metabolic syndrome, high blood pressure, type 2 diabetes, depression, anxiety, and many types of cancer.
- **Improves Mood**: Physical activity stimulates various brain chemicals that may leave you feeling happier, more relaxed, and less anxious.
- **Boosts Energy**: Regular physical activity can improve muscle strength and boost endurance.
- **Promotes Better Sleep**: Regular physical activity can help you fall asleep faster and deepen your sleep.

![Exercise Benefits](https://www.health.harvard.edu/media/content/images/cr/Exercise_and_fitness/18_Health_Benefits_of_Regular_Exercise.jpg)

### 🥗 The Importance of Eating Healthy

**1. Provides Essential Nutrients:**
- A balanced diet provides the nutrients your body needs to work effectively. Without balanced nutrition, your body is more prone to disease, infection, fatigue, and low performance.

**2. Reduces Risk of Chronic Diseases:**
- Eating a diet rich in fruits, vegetables, whole grains, and low-fat dairy products can help reduce the risk of heart disease, diabetes, and cancer.

**3. Supports Mental Health:**
- A healthy diet can help prevent depression and anxiety. Nutrient-rich foods like fruits, vegetables, and whole grains can help improve mood and mental well-being.

**4. Boosts Immune System:**
- Foods rich in vitamins and minerals, such as fruits and vegetables, can help strengthen your immune system and keep illnesses at bay.

![Healthy Eating](https://www.helpguide.org/wp-content/uploads/fast-foods-candy-cookies-pastries-768.jpg)

### 🏃‍♀️ Effective Exercise Routines

**1. Aerobic Exercise:**
- **Examples**: Walking, running, cycling, swimming, and dancing.
- **Benefits**: Improves cardiovascular health, burns calories, and aids in weight loss.

**2. Strength Training:**
- **Examples**: Weight lifting, resistance band exercises, and body-weight exercises like push-ups and squats.
- **Benefits**: Builds muscle mass, strengthens bones, and boosts metabolism.

**3. Flexibility Exercises:**
- **Examples**: Yoga, Pilates, and stretching exercises.
- **Benefits**: Enhances flexibility, improves posture, and reduces the risk of injuries.

**4. Balance Exercises:**
- **Examples**: Tai Chi, balance board exercises, and single-leg stands.
- **Benefits**: Improves balance and coordination, which can help prevent falls, especially in older adults.

![Exercise Routines](https://www.acsm.org/docs/default-source/files-for-resource-library/infographic/physical-activity-and-exercise-infographic.jpg)

### 🍎 Healthy Eating Tips

**1. Eat a Variety of Foods:**
- Include a wide range of foods in your diet to ensure you're getting all the necessary nutrients.

**2. Portion Control:**
- Be mindful of portion sizes to avoid overeating. Use smaller plates, bowls, and glasses.

**3. Limit Processed Foods:**
- Reduce the intake of processed foods high in sugar, salt, and unhealthy fats.

**4. Stay Hydrated:**
- Drink plenty of water throughout the day to stay hydrated and support bodily functions.

**5. Plan Your Meals:**
- Plan your meals ahead of time to ensure you're eating balanced and nutritious foods.

**6. Include Whole Grains:**
- Choose whole grains over refined grains. Whole grains provide more nutrients and fiber.

**7. Increase Fruits and Vegetables:**
- Aim to fill half your plate with fruits and vegetables at each meal.

**8. Choose Lean Proteins:**
- Opt for lean protein sources such as chicken, fish, beans, and legumes.

![Healthy Eating Tips](https://www.eatright.org/-/media/eatrightimages/nutritiontipsheets/101/1018tipsforeatingwell.jpg)

### 💪 Combining Exercise and Healthy Eating for Optimal Health

**1. Create a Balanced Routine:**
- Incorporate a mix of aerobic, strength, flexibility, and balance exercises into your weekly routine.

**2. Set Realistic Goals:**
- Set achievable goals for both exercise and eating habits. Track your progress and celebrate your successes.

**3. Listen to Your Body:**
- Pay attention to how your body feels during and after exercise and eating. Make adjustments as needed to ensure you're feeling your best.

**4. Stay Consistent:**
- Consistency is key to seeing long-term results. Make exercise and healthy eating a regular part of your lifestyle.

**5. Seek Support:**
- Join a fitness class, find a workout buddy, or consult a nutritionist to stay motivated and get personalized advice.

![Healthy Lifestyle](https://www.cdc.gov/diabetes/images/managing/images/diabetes-healthy-living-800px.jpg)

### 📈 Tracking Your Progress

**1. Keep a Food Diary:**
- Track what you eat and drink each day to stay mindful of your eating habits.

**2. Use Fitness Apps:**
- Utilize fitness apps to monitor your physical activity, set goals, and track your progress.

**3. Regular Check-Ups:**
- Schedule regular check-ups with your healthcare provider to monitor your health and make necessary adjustments to your diet and exercise routine.

### 📝 Conclusion
A healthy lifestyle is within your reach. By incorporating regular exercise and healthy eating into your daily routine, you can improve your overall health, reduce the risk of chronic diseases, and enjoy a better quality of life. Start today and take the first step towards a healthier you.
""")
elif sidebar_choice == 'Cholesterol':
st.subheader('Cholesterol Management')

# Flash the user with engaging information about cholesterol
st.markdown("""
### 🥼 Understanding Cholesterol
Cholesterol is a waxy substance found in your blood. Your body needs cholesterol to build healthy cells, but high levels of cholesterol can increase your risk of heart disease. Here's why managing cholesterol is crucial:

![Cholesterol](https://www.heart.org/-/media/Healthy-Living-Images/Cholesterol/Cholesterol-101-Infographic.jpg)

**Types of Cholesterol:**
- **Low-Density Lipoprotein (LDL)**: Known as "bad" cholesterol. High levels of LDL cholesterol can lead to plaque buildup in arteries and result in heart disease and stroke.
- **High-Density Lipoprotein (HDL)**: Known as "good" cholesterol. HDL cholesterol helps remove LDL cholesterol from the arteries.
- **Triglycerides**: A type of fat in the blood. High levels of triglycerides can also increase the risk of heart disease.

![Types of Cholesterol](https://www.cdc.gov/cholesterol/images/what-is-cholesterol-800.jpg)

### 💡 Why Cholesterol Matters

**1. Prevents Heart Disease:**
- High cholesterol levels can lead to atherosclerosis, a condition where arteries become narrowed and hardened due to plaque buildup.

**2. Reduces Stroke Risk:**
- Managing cholesterol levels can reduce the risk of stroke, as high cholesterol can lead to blocked arteries in the brain.

**3. Improves Overall Health:**
- Maintaining healthy cholesterol levels supports overall cardiovascular health and reduces the risk of other related diseases.

### 🩺 How to Manage Cholesterol Levels

**1. Eat Heart-Healthy Foods:**
- **Reduce Saturated Fats**: Found primarily in red meat and full-fat dairy products. Lowering your intake of saturated fats can reduce LDL cholesterol.
- **Eliminate Trans Fats**: Often found in margarines and store-bought cookies, crackers, and cakes.
- **Increase Omega-3 Fatty Acids**: Found in salmon, mackerel, and flaxseeds. Omega-3s don't affect LDL cholesterol but have other heart benefits.
- **Eat More Soluble Fiber**: Found in foods like oatmeal, kidney beans, Brussels sprouts, apples, and pears.

![Heart-Healthy Foods](https://www.heart.org/-/media/Healthy-Living-Images/Cholesterol/Cholesterol-Food.jpg)

**2. Exercise Regularly:**
- **Aerobic Exercise**: At least 30 minutes of moderate-intensity exercise, such as brisk walking, on most days of the week.
- **Strength Training**: Incorporate strength training exercises at least twice a week.

**3. Quit Smoking:**
- Quitting smoking improves your HDL cholesterol level and benefits your heart and lung health.

**4. Lose Weight:**
- Even a small amount of weight loss can help reduce cholesterol levels.

**5. Drink Alcohol Only in Moderation:**
- Moderate use of alcohol has been linked with higher levels of HDL cholesterol, but the benefits aren't strong enough to recommend alcohol for anyone who doesn't already drink.

### 🍽️ Diet and Cholesterol

**1. Foods to Avoid:**
- **Trans Fats**: Found in many fried foods and commercial baked products.
- **Saturated Fats**: Found in fatty cuts of meat, poultry with skin, and full-fat dairy products.
- **Cholesterol-Rich Foods**: Found in animal products like liver and other organ meats, egg yolks, and whole milk dairy products.

**2. Foods to Include:**
- **Nuts**: Almonds, walnuts, and other nuts can improve blood cholesterol.
- **Oats and Barley**: Contain soluble fiber that can reduce LDL cholesterol.
- **Fruits and Vegetables**: High in dietary fiber and low in calories.

![Cholesterol Diet](https://www.cdc.gov/cholesterol/images/how-can-i-prevent-high-cholesterol-800.jpg)

### 🏥 Medical Interventions

**1. Medications:**
- **Statins**: These drugs can lower LDL cholesterol and have other beneficial effects on the heart.
- **Cholesterol Absorption Inhibitors**: These medications help reduce cholesterol absorption from food.
- **Bile-Acid-Binding Resins**: These drugs can help lower LDL cholesterol.

**2. Regular Cholesterol Screening:**
- It's important to have your cholesterol levels checked regularly, as high cholesterol typically does not cause any symptoms.

### 📝 Conclusion
Managing your cholesterol is a key part of maintaining heart health and reducing the risk of serious cardiovascular events. By making dietary changes, increasing physical activity, quitting smoking, and following medical advice, you can effectively control your cholesterol levels and improve your overall health.

![Conclusion](https://www.heart.org/-/media/Healthy-Living-Images/Cholesterol/Cholesterol-Happy-Heart.jpg)
""")
elif sidebar_choice == 'High Blood Pressure':
st.subheader('High Blood Pressure Management')


# Flash the user with engaging information about high blood pressure
st.markdown("""
### 💓 Understanding High Blood Pressure (Hypertension)
High blood pressure, or hypertension, is a common condition where the force of the blood against your artery walls is high enough that it may eventually cause health problems, such as heart disease. Here’s why managing high blood pressure is crucial:

![High Blood Pressure](https://www.cdc.gov/bloodpressure/images/BloodPressure_Infographic.jpg)

**Why High Blood Pressure Matters:**
- **Heart Disease and Stroke**: High blood pressure can lead to hardening and thickening of the arteries (atherosclerosis), which can result in heart attack, stroke, or other complications.
- **Aneurysm**: Increased blood pressure can cause your blood vessels to weaken and bulge, forming an aneurysm. If an aneurysm ruptures, it can be life-threatening.
- **Heart Failure**: To pump blood against the higher pressure in your vessels, the heart has to work harder. This causes the walls of the heart's pumping chamber to thicken (left ventricular hypertrophy). Eventually, the thickened muscle may have a hard time pumping enough blood to meet your body's needs, which can lead to heart failure.
- **Weakened and Narrowed Blood Vessels in Your Kidneys**: This can prevent these organs from functioning normally.
- **Thickened, Narrowed, or Torn Blood Vessels in the Eyes**: This can result in vision loss.

### 🔍 Recognizing High Blood Pressure

**Symptoms of Severe Hypertension:**
- Severe headaches
- Nosebleed
- Fatigue or confusion
- Vision problems
- Chest pain
- Difficulty breathing
- Irregular heartbeat
- Blood in the urine
- Pounding in your chest, neck, or ears

**Note**: Most people with high blood pressure have no signs or symptoms, even if blood pressure readings reach dangerously high levels.

### 🩺 How to Manage High Blood Pressure

**1. Eat a Healthy Diet:**
- **Reduce Sodium in Your Diet**: Aim to limit sodium to less than 2,300 milligrams (mg) a day or less. However, a lower sodium intake — 1,500 mg a day or less — is ideal for most adults.
- **Increase Potassium**: Foods rich in potassium, such as fruits and vegetables, can lessen the effects of sodium on blood pressure.
- **Eat Plenty of Fruits and Vegetables**: The DASH (Dietary Approaches to Stop Hypertension) diet is a recommended eating plan to lower or control high blood pressure.

![Healthy Diet](https://www.heart.org/-/media/Healthy-Living-Images/Healthy-Eating/dash-diet-750x420.jpg)

**2. Exercise Regularly:**
- Regular physical activity — such as 150 minutes a week, or about 30 minutes most days of the week — can lower your blood pressure by about 5 to 8 mm Hg if you have high blood pressure.
- **Aerobic Exercise**: Walking, jogging, cycling, swimming, or dancing.
- **Strength Training**: Incorporate strength training exercises at least twice a week.

**3. Maintain a Healthy Weight:**
- Losing even a small amount of weight if you're overweight or obese can help reduce your blood pressure.

**4. Limit Alcohol and Avoid Tobacco:**
- Drinking alcohol in moderation is generally fine, but drinking too much alcohol can raise your blood pressure.
- Avoid tobacco products and secondhand smoke. The chemicals in tobacco can increase your blood pressure and damage your heart.

**5. Reduce Stress:**
- **Relaxation Techniques**: Practice relaxation or slow, deep breathing techniques.
- **Physical Activity**: Exercise regularly to help manage stress.
- **Get Enough Sleep**: Quality sleep can play a part in managing blood pressure.

![Manage Stress](https://www.verywellmind.com/thmb/Y_sTXzC8G5sdLQBhT6dD0FwWxk8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/how-to-relax-3144917-00ee9b849a614ab09d6a1608b5099ab5.png)

### 🍽️ High Blood Pressure Diet Tips

**1. Focus on Whole Foods:**
- Eat a variety of fresh fruits, vegetables, and whole grains.

**2. Reduce Processed Foods:**
- Minimize the intake of processed and pre-packaged foods that are high in salt, fat, and sugar.

**3. Healthy Fats:**
- Include healthy fats from sources like avocados, nuts, and olive oil.

**4. Limit Sugar and Refined Carbs:**
- Reduce your consumption of sugary beverages, candies, and refined carbs that can lead to weight gain and higher blood pressure.

![Healthy Diet](https://www.helpguide.org/wp-content/uploads/table-with-grains-vegetables-fruit-768.jpg)

### 🏥 Medical Interventions

**1. Medications:**
- **Diuretics**: Help your kidneys remove sodium and water from your body.
- **ACE Inhibitors**: Help relax blood vessels by blocking the formation of a natural chemical that narrows blood vessels.
- **Calcium Channel Blockers**: Help relax the muscles of your blood vessels.
- **Beta Blockers**: Reduce the workload on your heart and open your blood vessels, causing your heart to beat slower and with less force.

**2. Regular Monitoring:**
- Keep track of your blood pressure at home and have regular check-ups with your healthcare provider to ensure your treatment plan is working.

### 📝 Conclusion
Managing high blood pressure is crucial for maintaining overall health and preventing serious cardiovascular events. By adopting a healthy lifestyle, making dietary changes, engaging in regular physical activity, and following medical advice, you can effectively control your blood pressure and enhance your quality of life.

![Conclusion](https://www.heart.org/-/media/Healthy-Living-Images/Heart-Health/heart-health.jpg)
""")
elif sidebar_choice == 'Exercise Routine Generator':
st.subheader('Personalized Exercise Routine Generator')


st.markdown("""
### 🏃‍♂️ Create Your Exercise Routine
Generate a personalized exercise routine to help you stay active and manage diabetes.

**Step 1: Enter Your Details**
""")

# Collect user details
age = st.number_input('Enter your age:', min_value=10, max_value=100)
weight = st.number_input('Enter your weight (in kg):', min_value=30, max_value=200)
height = st.number_input('Enter your height (in cm):', min_value=100, max_value=250)
gender = st.selectbox('Select your gender:', ['Male', 'Female', 'Other'])
fitness_level = st.selectbox('Select Your Fitness Level:', ['Beginner', 'Intermediate', 'Advanced'])
goals = st.multiselect('Select Your Goals:', ['Weight Loss', 'Muscle Building', 'Cardiovascular Health', 'Flexibility and Balance', 'Overall Fitness'])

if st.button('Generate Routine'):
    st.markdown("""
    **Personalized Exercise Routine:**
    """)

    if 'Weight Loss' in goals:
        st.markdown("""
        **Focus on Weight Loss:**
        
        **Monday**: 
        - **Cardio**: 30 minutes of brisk walking
        - **Strength Training**: Body-weight exercises (squats, push-ups, lunges) - 2 sets of 12 reps each

        **Wednesday**: 
        - **Cardio**: 30 minutes of cycling
        - **Flexibility**: 15 minutes of stretching exercises

        **Friday**: 
        - **Cardio**: 30 minutes of jogging
        - **Strength Training**: Light weights (bicep curls, shoulder press) - 2 sets of 12 reps each

        **Sunday**: 
        - **Flexibility**: 20 minutes of yoga or Pilates

        ![Weight Loss Exercise](https://www.verywellfit.com/thmb/4z9Gcs0Ah1KgR8tRdmZ8kZkHh6U=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-539582400-5c7d7f9e46e0fb00012f69cf.jpg)
        """)

    if 'Muscle Building' in goals:
        st.markdown("""
        **Focus on Muscle Building:**
        
        **Monday**: 
        - **Strength Training**: Compound exercises (squats, deadlifts, bench press) - 4 sets of 8 reps each
        - **Cardio**: 15 minutes of HIIT (High-Intensity Interval Training)

        **Wednesday**: 
        - **Strength Training**: Upper body (pull-ups, rows, shoulder press) - 4 sets of 10 reps each
        - **Flexibility**: 20 minutes of dynamic stretching exercises

        **Friday**: 
        - **Strength Training**: Lower body (leg press, lunges, calf raises) - 4 sets of 10 reps each
        - **Cardio**: 20 minutes of moderate-intensity cycling

        **Sunday**: 
        - **Flexibility**: 25 minutes of advanced yoga poses

        ![Muscle Building Exercise](https://www.verywellfit.com/thmb/1sWyrmgOlyr3SDjUy7yS4pLDG1I=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-915985742-5c3bd73846e0fb0001ea14a0.jpg)
        """)

    if 'Cardiovascular Health' in goals:
        st.markdown("""
        **Focus on Cardiovascular Health:**
        
        **Monday**: 
        - **Cardio**: 40 minutes of running or brisk walking
        - **Strength Training**: Light weights (circuit training) - 3 sets of 15 reps each

        **Wednesday**: 
        - **Cardio**: 45 minutes of swimming
        - **Flexibility**: 15 minutes of stretching exercises

        **Friday**: 
        - **Cardio**: 40 minutes of cycling or rowing
        - **Strength Training**: Body-weight exercises (push-ups, planks) - 3 sets of 15 reps each

        **Sunday**: 
        - **Flexibility**: 30 minutes of yoga

        ![Cardiovascular Health Exercise](https://www.verywellfit.com/thmb/RuIuQ71mSgeWJGHviRaG-v_A-Jc=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1046990574-5c7d7f6a46e0fb00013f7ff7.jpg)
        """)

    if 'Flexibility and Balance' in goals:
        st.markdown("""
        **Focus on Flexibility and Balance:**
        
        **Monday**: 
        - **Flexibility**: 20 minutes of yoga
        - **Balance**: 15 minutes of balance board exercises

        **Wednesday**: 
        - **Flexibility**: 25 minutes of Pilates
        - **Balance**: 20 minutes of Tai Chi

        **Friday**: 
        - **Flexibility**: 30 minutes of advanced stretching exercises
        - **Balance**: 20 minutes of single-leg stands and other balance exercises

        **Sunday**: 
        - **Flexibility and Balance**: 40 minutes of combined yoga and Tai Chi

        ![Flexibility and Balance Exercise](https://www.verywellfit.com/thmb/xF57S_zK3Rsa8JeGJ2xkMUsNe00=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-944650668-5c3bd6c846e0fb00012a2e7d.jpg)
        """)

    if 'Overall Fitness' in goals:
        st.markdown("""
        **Focus on Overall Fitness:**
        
        **Monday**: 
        - **Cardio**: 30 minutes of moderate-intensity running
        - **Strength Training**: Full-body workout (squats, push-ups, rows) - 3 sets of 12 reps each

        **Wednesday**: 
        - **Cardio**: 30 minutes of swimming
        - **Flexibility**: 20 minutes of stretching exercises

        **Friday**: 
        - **Cardio**: 30 minutes of cycling
        - **Strength Training**: Circuit training (light weights and body-weight exercises) - 3 sets of 15 reps each

        **Sunday**: 
        - **Flexibility**: 25 minutes of yoga or Pilates

        ![Overall Fitness Exercise](https://www.verywellfit.com/thmb/fnGQz0mYX7qF4VEC8h5X9w-omA0=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1048946218-5c7d8e5546e0fb0001ea1735.jpg)
        """)

    st.write("Please consult with a healthcare provider before starting any new exercise routine to ensure it's safe and appropriate for your health condition.")
elif sidebar_choice == 'Mindfulness and Stress Management':
st.subheader('Mindfulness and Stress Management')

st.markdown("""
### 🧘‍♀️ Manage Stress and Practice Mindfulness
Learn techniques to reduce stress and improve your mental health, which can positively impact diabetes management.

**Step 1: Understand the Benefits**
- Reduces blood sugar levels
- Lowers blood pressure
- Improves mood and mental well-being

![Mindfulness](https://www.verywellmind.com/thmb/G-2pS1LOX8qzLxQF5Ol2jipVVAE=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1010198702-5c516dd4c9e77c0001f08d5c.jpg)

### 🌟 Techniques to Practice Mindfulness

**1. Meditation**
- **Guided Meditation**: Use apps or online resources to follow guided meditation sessions.
- **Breathing Meditation**: Focus on your breath, inhaling and exhaling slowly. Count each breath if it helps you concentrate.
- **Body Scan Meditation**: Focus on different parts of your body, from your toes to your head, noticing any tension and letting it go.

![Meditation](https://www.verywellmind.com/thmb/JGkxEl1B4NVG1m03Dh6v1bhyUuI=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1170782157-5e8b0ab6c4e1a3b21f50fa29.jpg)

**2. Deep Breathing Exercises**
- **Box Breathing**: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds, and hold for 4 seconds. Repeat several times.
- **4-7-8 Breathing**: Inhale for 4 seconds, hold for 7 seconds, and exhale for 8 seconds. This technique can help calm the mind and body.
- **Diaphragmatic Breathing**: Place one hand on your chest and the other on your abdomen. Breathe deeply so that your abdomen rises more than your chest.

![Deep Breathing](https://www.verywellmind.com/thmb/EjG4g14QeHKY9OBfhmsfU5XN9Xk=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1154776458-5d8e51c346e0fb0001e443e8.jpg)

**3. Progressive Muscle Relaxation**
- Tense and relax different muscle groups in your body, starting from your toes and working up to your head. This helps release physical tension and promotes relaxation.

![Progressive Muscle Relaxation](https://www.verywellmind.com/thmb/_px5Mt7wJr3T8Yhd2y4JEMvTnno=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1144138055-5c516e2046e0fb0001e3b8cc.jpg)

**4. Mindful Eating**
- Pay attention to what you eat, savoring each bite. Notice the flavors, textures, and sensations. This can help you enjoy your food more and prevent overeating.

![Mindful Eating](https://www.verywellfit.com/thmb/b5h4Reb8X0P2lt4Um0lNgbd-8_k=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-927619572-5c48d9e7c9e77c0001eb7335.jpg)

**5. Visualization**
- Close your eyes and imagine a peaceful place, such as a beach or a forest. Use all your senses to make the scene as vivid as possible. This can help reduce stress and improve your mood.

![Visualization](https://www.verywellmind.com/thmb/rf0vDLnvNehVbgd9NYy13lXZdf8=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-825443688-5c516ddbc9e77c0001f08d65.jpg)

### 📝 Create a Mindfulness Routine

**1. Set Aside Time Each Day**
- Schedule a specific time each day for mindfulness practices. Even just 10-15 minutes can make a difference.

**2. Create a Peaceful Environment**
- Find a quiet, comfortable place where you won't be disturbed. You can enhance the environment with soothing music, candles, or essential oils.

**3. Be Consistent**
- Consistency is key to reaping the benefits of mindfulness. Make it a part of your daily routine.

**4. Keep a Journal**
- Write about your mindfulness practice and how it makes you feel. Reflect on any changes in your mood or stress levels.

![Mindfulness Routine](https://www.verywellmind.com/thmb/yRReoMXqF8cw1y0HXs_PpHdXEas=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-637246080-5c516e2b46e0fb0001e3b8d7.jpg)

### 💡 Additional Tips for Stress Management

**1. Physical Activity**
- Exercise regularly to reduce stress and improve overall health. Activities like walking, yoga, and dancing can be particularly beneficial.

**2. Healthy Eating**
- Eat a balanced diet to support your physical and mental well-being. Avoid excessive caffeine and sugar, which can increase anxiety.

**3. Social Connections**
- Spend time with friends and family. Social support can help you cope with stress and improve your mood.

**4. Sleep Well**
- Ensure you get enough sleep each night. Good sleep hygiene includes maintaining a regular sleep schedule and creating a restful environment.

**5. Seek Professional Help**
- If stress becomes overwhelming, consider seeking help from a mental health professional. Therapy and counseling can provide valuable support and strategies.

![Stress Management](https://www.verywellmind.com/thmb/YNIB55HSZ9G9jUQ6GzkxvPvqGUM=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-512298302-5c4a729746e0fb0001ef4e61.jpg)

### 📆 Schedule Your Mindfulness Practices
Use the calendar below to schedule your mindfulness practices and set reminders to help you stay consistent.
""")

# Interactive tools and functionality for scheduling
practice_date = st.date_input('Select a date for your practice')
practice_time = st.time_input('Select a time for your practice')

if st.button('Add to Schedule'):
    st.write(f'Scheduled practice on {practice_date} at {practice_time}')

# Display scheduled practices
st.write('Your Scheduled Practices:')
st.write(f'Practice on {practice_date} at {practice_time}')
elif sidebar_choice == 'Meal Planner':
st.subheader('Healthy Meal Planner')

st.markdown("""
### 🍽️ Plan Your Meals for a Healthy Lifestyle
Use this tool to create a balanced meal plan that meets your dietary needs and helps manage or prevent diabetes.

**Step 1: Select Your Dietary Preferences**
""")

# Collect user dietary preferences
dietary_preferences = st.multiselect('Select your dietary preferences:', 
                                     ['Vegetarian', 'Vegan', 'Gluten-Free', 'Low Carb', 'High Protein'])

st.markdown("""
**Step 2: Choose Your Meals**
""")

# Example meal options
meal_options = {
    'Breakfast': ['Smoothie', 'Oatmeal', 'Eggs', 'Avocado Toast', 'Yogurt with Berries'],
    'Lunch': ['Salad', 'Sandwich', 'Soup', 'Grilled Chicken', 'Quinoa Salad'],
    'Dinner': ['Baked Salmon', 'Veggie Stir-fry', 'Pasta', 'Grilled Tofu', 'Steak'],
    'Snacks': ['Nuts', 'Fruits', 'Yogurt', 'Granola Bar', 'Vegetable Sticks']
}

# Select meals for each meal time
selected_breakfast = st.selectbox('Select a breakfast:', meal_options['Breakfast'])
selected_lunch = st.selectbox('Select a lunch:', meal_options['Lunch'])
selected_dinner = st.selectbox('Select a dinner:', meal_options['Dinner'])
selected_snacks = st.multiselect('Select snacks:', meal_options['Snacks'])

st.markdown("""
**Step 3: Generate Your Meal Plan**
- Get personalized recipes and a shopping list.
""")

if st.button('Generate Meal Plan'):
    st.markdown(f"""
    ### Your Personalized Meal Plan
    **Breakfast**: {selected_breakfast}

    **Lunch**: {selected_lunch}

    **Dinner**: {selected_dinner}

    **Snacks**: {', '.join(selected_snacks)}
    """)

st.markdown("""
### 📆 Set Meal Reminders
Use the tools below to set reminders for your meals.
""")

# Interactive tools for setting meal reminders
breakfast_time = st.time_input('Set a time for breakfast:')
lunch_time = st.time_input('Set a time for lunch:')
dinner_time = st.time_input('Set a time for dinner:')
snack_times = [st.time_input(f'Set a time for snack {i + 1}:') for i in range(len(selected_snacks))]

if st.button('Set Reminders'):
    st.markdown(f"""
    ### Your Meal Reminders
    - **Breakfast**: {breakfast_time}
    - **Lunch**: {lunch_time}
    - **Dinner**: {dinner_time}
    - **Snacks**: {', '.join([str(time) for time in snack_times])}
    """)

st.markdown("""
### 📝 Example Recipes
Here are some example recipes for your selected meals:

**Breakfast: {selected_breakfast}**
- **Smoothie**: Blend together a banana, a handful of spinach, 1 cup of almond milk, and a tablespoon of peanut butter.
- **Oatmeal**: Cook oats with water or milk, and top with fresh berries, a drizzle of honey, and a sprinkle of nuts.

**Lunch: {selected_lunch}**
- **Salad**: Mix greens, cherry tomatoes, cucumbers, and grilled chicken, and dress with olive oil and lemon juice.
- **Sandwich**: Layer whole grain bread with avocado, turkey slices, lettuce, and tomato.

**Dinner: {selected_dinner}**
- **Baked Salmon**: Season salmon with salt, pepper, and lemon juice. Bake at 200°C for 15-20 minutes. Serve with steamed vegetables.
- **Veggie Stir-fry**: Sauté a mix of bell peppers, broccoli, carrots, and tofu in a soy sauce and garlic sauce.

**Snacks: {', '.join(selected_snacks)}**
- **Nuts**: A handful of almonds or walnuts.
- **Fruits**: An apple or a banana.
- **Yogurt**: A cup of Greek yogurt with a drizzle of honey.
- **Granola Bar**: A homemade or store-bought granola bar.
- **Vegetable Sticks**: Carrot and celery sticks with hummus.

![Healthy Meal](https://www.eatright.org/-/media/homeimages/eatrightimages/food/nutrition/vegetarianandvegan/healthymealpreparation.jpg)
""")
elif sidebar_choice == 'Initiatives':
st.subheader('Community Initiatives and Volunteering')

st.markdown("""
### 🤝 Get Involved in Community Initiatives
Participate in community initiatives to help raise awareness about diabetes, support those affected, and contribute to a healthier society. Below are some initiatives you can join.

![Community Initiatives](https://www.verywellmind.com/thmb/xF57S_zK3Rsa8JeGJ2xkMUsNe00=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-944650668-5c3bd6c846e0fb00012a2e7d.jpg)
""")

# List of initiatives
initiatives = [
    {
        "title": "Diabetes Awareness Walk",
        "description": "Join us for a walk to raise awareness about diabetes and promote a healthy lifestyle.",
        "date": "June 25, 2024",
        "location": "Central Park, New York"
    },
    {
        "title": "Healthy Cooking Workshop",
        "description": "Learn to cook healthy meals that can help manage and prevent diabetes.",
        "date": "July 10, 2024",
        "location": "Community Center, Los Angeles"
    },
    {
        "title": "Fitness Bootcamp",
        "description": "Participate in a fitness bootcamp designed to promote physical activity and healthy living.",
        "date": "August 5, 2024",
        "location": "Beachside Park, Miami"
    }
]

for initiative in initiatives:
    st.markdown(f"""
    ### {initiative['title']}
    **Description**: {initiative['description']}
    **Date**: {initiative['date']}
    **Location**: {initiative['location']}
    """)
    
    if st.button(f"Apply Now for {initiative['title']}"):
        st.markdown(f"""
        ### Application Form for {initiative['title']}
        """)
        # Application form
        name = st.text_input('Name')
        email = st.text_input('Email')
        phone = st.text_input('Phone')
        why_volunteer = st.text_area('Why do you want to volunteer for this initiative?')

        if st.button('Submit Application'):
            st.markdown("""
            **Thank you for applying! We will review your application and get back to you soon.**
            """)
            # Save the application details (this is a placeholder, actual implementation would save to a database)
            application_details = {
                'name': name,
                'email': email,
                'phone': phone,
                'initiative': initiative['title'],
                'why_volunteer': why_volunteer
            }
            st.write(application_details)
elif sidebar_choice == 'Medication Management':
st.subheader('Medication Management')
st.markdown("### Customized Medication Management for Seniors")

st.write("Managing your medications can be made easier with a few simple steps. Use the interactive tools below to help you stay organized and on track.")

st.markdown("#### 1. Create Your Medication List")
medication_name = st.text_input("Enter the name of your medication", key="med_name")
dosage = st.text_input("Enter the dosage (e.g., 50mg)", key="dosage")
frequency = st.text_input("Enter the frequency (e.g., Twice a day)", key="frequency")

if 'medications' not in st.session_state:
    st.session_state.medications = []

if st.button("Add Medication"):
    st.session_state.medications.append({
        'name': medication_name,
        'dosage': dosage,
        'frequency': frequency
    })
    st.success("Medication added successfully!")

st.write("### Your Medications")
if st.session_state.medications:
    for med in st.session_state.medications:
        st.write(f"- **Medication:** {med['name']}, **Dosage:** {med['dosage']}, **Frequency:** {med['frequency']}")
else:
    st.write("No medications added yet.")

st.markdown("#### 2. Set Medication Reminders")
st.write("Use reminders to ensure you take your medications on time.")

reminder_time = st.time_input("Set a reminder time")
reminder_frequency = st.selectbox("Reminder frequency", ["Daily", "Weekly", "Monthly"])
reminder_note = st.text_input("Reminder note (optional)", key="reminder_note")

if st.button("Set Reminder"):
    st.success(f"Reminder set for {reminder_time} {reminder_frequency} with note: {reminder_note}")
    st.info("Receive a small gift for consistently taking your medications for a month! 🎁")

st.markdown("#### 3. Track Your Medication Progress")
st.write("Track your medication adherence to stay on top of your health.")
progress = st.slider("Medication Adherence Progress", 0, 100, 0)

if progress < 50:
    st.warning("Your medication adherence is below 50%. Consider setting more reminders.")
elif 50 <= progress < 80:
    st.info("Your medication adherence is between 50% and 80%. Keep it up!")
else:
    st.success("Great job! Your medication adherence is above 80%. You’re eligible for a special discount on your next purchase!")

st.markdown("#### 4. Medication Management Tips")
st.write("- **Use a Pill Organizer**: A pill organizer can help you keep track of your medications and ensure you take them as prescribed.")
st.write("- **Set Alarms**: Use alarms or reminders on your phone or clock to remind you to take your medications.")
st.write("- **Review Medications with Your Doctor**: Regularly review your medications with your healthcare provider to ensure they are still appropriate for you.")
st.write("- **Report Side Effects**: Inform your doctor of any side effects or issues with your medications.")

st.markdown("#### 5. Additional Resources")
st.write("Explore these resources for more information on medication management:")
st.write("- [Medication Management Tips for Older Adults](https://www.healthinaging.org/tools-and-tips/medication-safety-older-adults)")
st.write("- [How to Use a Pill Organizer](https://www.fda.gov/drugs/special-features/your-medicines-be-smart-safe-and-seek-questions-about-using-pill-organizer-or-dosette-box)")
st.write("- [Understanding Medication Side Effects](https://www.mayoclinic.org/healthy-lifestyle/healthy-aging/in-depth/medication-side-effects/art-20048208)")
st.write("- [Benefits of Medication Management](https://www.cdc.gov/aging/pdf/cognitive-impairment-compendium.pdf)")

st.markdown("#### 6. Incentives for Staying on Track")
st.write("To encourage consistent medication adherence, we offer the following incentives:")
st.write("- **Monthly Gifts**: Receive a small gift, such as a wellness kit or a gift card, for consistently taking your medications for a month. This is our way of saying thank you for taking care of your health!")
st.write("- **Discounts**: Earn special discounts on health-related purchases, such as fitness equipment, vitamins, or health checkups, for maintaining high medication adherence. The higher your adherence, the bigger the discount!")
st.write("- **Health Tips**: Get personalized health tips based on your medication progress. These tips will help you manage your medications better, improve your overall health, and stay motivated on your health journey.")

st.markdown("#### 7. Easy Ways to Stay on Track")
st.write("To make it easier for you to manage your medications, we provide the following tools:")
st.write("- **Automated Reminders**: Set up automated reminders to take your medications on time. Choose your preferred method: phone alerts, text messages, or emails.")
st.write("- **Progress Tracking**: Track your medication adherence and receive feedback and incentives. The more consistent you are, the more rewards you earn!")
st.write("- **Doctor's Review**: Schedule regular reviews with your healthcare provider to ensure your medications are effective and appropriate. Your doctor can provide valuable insights and adjust your prescriptions if needed.")
st.write("- **Support Community**: Join a support community of other seniors managing their medications. Share tips, offer encouragement, and learn from each other's experiences. Together, we can make medication management easier and more enjoyable.")
elif sidebar_choice == 'Success Stories':
st.subheader('Success Stories')

python

st.markdown("""
### 🌟 Read and Share Success Stories
Get inspired by reading success stories from others who have successfully managed diabetes and improved their health. Share your own story to motivate others.

![Success Stories](https://www.diabetes.org/sites/default/files/styles/paragraph_half_width_600/public/2020-12/diabetes_story.jpg)
""")

# Sample success stories
success_stories = [
    {
        "name": "John Doe",
        "story": "I was diagnosed with type 2 diabetes five years ago. With the help of this platform, I learned to manage my diet and exercise regularly. Today, my blood sugar levels are stable, and I feel healthier than ever.",
        "date": "March 15, 2024"
    },
    {
        "name": "Maria Smith",
        "story": "Quitting smoking was the hardest thing I've ever done, but it was worth it. The support and resources available on this platform made all the difference. My health has improved dramatically.",
        "date": "April 10, 2024"
    },
    {
        "name": "Paul Johnson",
        "story": "Through personalized meal plans and regular exercise routines provided here, I've lost 30 pounds and significantly reduced my diabetes symptoms. I'm grateful for this community.",
        "date": "May 5, 2024"
    }
]

for story in success_stories:
    st.markdown(f"""
    ### {story['name']}
    **Date**: {story['date']}
    **Story**: {story['story']}
    """)

st.markdown("""
### Share Your Success Story
""")
# Form to submit a success story
user_name = st.text_input('Your Name')
user_story = st.text_area('Your Success Story')
user_date = st.date_input('Date', value=None)

if st.button('Submit Your Story'):
    st.markdown("""
    **Thank you for sharing your story! It will inspire others to take charge of their health.**
    """)
    # Display the submitted story (in a real application, this would save to a database)
    new_story = {
        "name": user_name,
        "story": user_story,
        "date": user_date
    }
    st.write(new_story)
Running the Streamlit app
if name == "main":
# This block is not necessary since st.set_page_config() is already called at the beginning
pass
