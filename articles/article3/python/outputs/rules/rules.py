def findDecision(obj): #obj[0]: cap-shape, obj[1]: cap-surface, obj[2]: cap-color, obj[3]: bruises, obj[4]: gill-attachement, obj[5]: gill-spacing, obj[6]: gill-size, obj[7]: gill-color, obj[8]: stalk-shape, obj[9]: stalk-root, obj[10]: stalk-surface-above-ring, obj[11]: stalk-surface-bellow-ring, obj[12]: stalk-color-above-ring, obj[13]: stalk-color-bellow-ring, obj[14]: viel-type, obj[15]: veil-color, obj[16]: ring-number, obj[17]: ring-type, obj[18]: spore-print-color, obj[19]: population
   # {"feature": "gill-size", "instances": 8416, "metric_value": 0.9968, "depth": 1}
   if obj[6] == 'BROAD':
      # {"feature": "ring-type", "instances": 5880, "metric_value": 0.8685, "depth": 2}
      if obj[17] == 'PENDANT':
         # {"feature": "stalk-surface-above-ring", "instances": 3320, "metric_value": 0.4952, "depth": 3}
         if obj[10] == 'SMOOTH':
            # {"feature": "spore-print-color", "instances": 3016, "metric_value": 0.3719, "depth": 4}
            if obj[18] == 'BROWN':
               return 'EDIBLE'
            elif obj[18] == 'BLACK':
               return 'EDIBLE'
            elif obj[18] == 'WHITE':
               return 'EDIBLE'
            elif obj[18] == 'CHOCOLATE':
               return 'POISONOUS'
            elif obj[18] == 'GREEN':
               return 'POISONOUS'
            elif obj[18] == 'BUFF':
               return 'EDIBLE'
            elif obj[18] == 'YELLOW':
               return 'EDIBLE'
            elif obj[18] == 'ORANGE':
               return 'EDIBLE'
            else:
               return 'EDIBLE'
         elif obj[10] == 'SILKY':
            return 'EDIBLE'
         elif obj[10] == 'FIBROUS':
            return 'POISONOUS'
         elif obj[10] == 'SCALY':
            return 'EDIBLE'
         else:
            return 'EDIBLE'
      elif obj[17] == 'LARGE':
         return 'POISONOUS'
      elif obj[17] == 'EVANESCENT':
         return 'EDIBLE'
      elif obj[17] == 'NONE':
         return 'POISONOUS'
      else:
         return 'POISONOUS'
   elif obj[6] == 'NARROW':
      # {"feature": "gill-spacing", "instances": 2536, "metric_value": 0.538, "depth": 2}
      if obj[5] == 'CLOSE':
         # {"feature": "population", "instances": 2256, "metric_value": 0.3425, "depth": 3}
         if obj[19] == 'SEVERAL':
            # {"feature": "ring-type", "instances": 2008, "metric_value": 0.223, "depth": 4}
            if obj[17] == 'EVANESCENT':
               return 'POISONOUS'
            elif obj[17] == 'PENDANT':
               # {"feature": "bruises", "instances": 224, "metric_value": 0.7496, "depth": 5}
               if obj[3] == 'BRUISES':
                  return 'POISONOUS'
               elif obj[3] == 'NO':
                  # {"feature": "stalk-root", "instances": 96, "metric_value": 1.0, "depth": 6}
                  if obj[9] == 'EQUAL':
                     return 'EDIBLE'
                  elif obj[9] == 'BULBOUS':
                     return 'POISONOUS'
                  else:
                     return 'POISONOUS'
               else:
                  return 'EDIBLE'
            elif obj[17] == 'FLARING':
               return 'EDIBLE'
            else:
               return 'EDIBLE'
         elif obj[19] == 'SCATTERED':
            return 'POISONOUS'
         elif obj[19] == 'SOLITARY':
            return 'EDIBLE'
         else:
            return 'EDIBLE'
      elif obj[5] == 'CROWDED':
         # {"feature": "population", "instances": 280, "metric_value": 0.971, "depth": 3}
         if obj[19] == 'SEVERAL':
            # {"feature": "spore-print-color", "instances": 216, "metric_value": 0.7642, "depth": 4}
            if obj[18] == 'WHITE':
               return 'EDIBLE'
            elif obj[18] == 'BROWN':
               # {"feature": "bruises", "instances": 72, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'BRUISES':
                  return 'EDIBLE'
               elif obj[3] == 'NO':
                  return 'POISONOUS'
               else:
                  return 'POISONOUS'
            elif obj[18] == 'PURPLE':
               return 'EDIBLE'
            elif obj[18] == 'BLACK':
               return 'POISONOUS'
            else:
               return 'POISONOUS'
         elif obj[19] == 'SCATTERED':
            return 'POISONOUS'
         elif obj[19] == 'CLUSTERED':
            return 'POISONOUS'
         else:
            return 'POISONOUS'
      else:
         return 'EDIBLE'
   else:
      return 'POISONOUS'
