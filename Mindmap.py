from graphviz import Digraph

# Create the central topic node
central_topic = Digraph(name='Applications of Machine Learning in Tropical Cyclone Forecast Modeling')

# Create branches and sub-branches
applications = Digraph(name='Applications')
data_sources = Digraph(name='Data Sources')
challenges = Digraph(name='Challenges')
future_directions = Digraph(name='Future Directions')

# Add sub-branches to Applications
applications.node('Track Prediction', advantages='Improved accuracy, faster predictions\nDisadvantages: Limited lead time, data dependence')
applications.node('Intensity Prediction', advantages='Improved lead time for evacuation planning\nDisadvantages: Data limitations, model sensitivity')
applications.node('Rainfall Prediction', advantages='Better preparedness for flooding\nDisadvantages: Highly localized patterns, complex model requirements')
applications.node('Cyclone Genesis Prediction', advantages='Early warning system\nDisadvantages: Limited knowledge, data scarcity')

# Add sub-branches to Data Sources
data_sources.node('Numerical Model Data', advantages='Comprehensive information, well-established format\nDisadvantages: Potential biases, computational limitations')
data_sources.node('Satellite Data', advantages='Real-time observations, global coverage\nDisadvantages: Missing data, limited resolution')
data_sources.node('Historical Records', advantages='Long-term trends, insights into past events\nDisadvantages: Limited to past scenarios, potential data inconsistency')

# Add sub-branches to Challenges
challenges.node('Data Availability and Quality', details='Limited historical data, inconsistent formats, missing observations')
challenges.node('Model Complexity and Interpretability', details='Balancing accuracy with user understanding')
challenges.node('Computational Constraints', details='Real-time processing requirements, resource limitations')
challenges.node('Ethical Considerations', details='Bias in data or algorithms, potential misuse of predictions')

# Add sub-branches to Future Directions
future_directions.node('Improved Data Collection and Sharing', details='Standardizing formats, integrating diverse sources')
future_directions.node('Advanced Machine Learning Techniques', details='Deep learning, ensemble models, explainable AI')
future_directions.node('Collaborative Research and Development', details='Addressing challenges, improving forecasting capabilities')

# Connect branches to the central topic
central_topic.subgraph(applications)
central_topic.subgraph(data_sources)
central_topic.subgraph(challenges)
central_topic.subgraph(future_directions)

# Render the mind map to a PNG image
central_topic.render('mindmap.png', view=True)

print("Mind map created successfully!")
