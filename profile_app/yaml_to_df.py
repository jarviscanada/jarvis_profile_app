import yaml
import pandas as pd

profile = None
with open("/Users/ewang/dev/jrvs/jarvis_profile_app/data/profile.yaml") as f:
    profile = yaml.load(f,yaml.FullLoader)

n_profile = pd.json_normalize(profile)
print(n_profile.columns)





#df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
#df.loc['viper'] = {"max_speed": 0, "shield": 1}
#print(df)
exit






