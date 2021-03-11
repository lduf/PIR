def findDecision(obj): #obj[0]: cap-shape, obj[1]: cap-surface, obj[2]: cap-color, obj[3]: bruises, obj[4]: odor, obj[5]: gill-attachement, obj[6]: gill-spacing, obj[7]: gill-size, obj[8]: gill-color, obj[9]: stalk-shape, obj[10]: stalk-root, obj[11]: stalk-surface-above-ring, obj[12]: stalk-surface-bellow-ring, obj[13]: stalk-color-above-ring, obj[14]: stalk-color-bellow-ring, obj[15]: viel-type, obj[16]: veil-color, obj[17]: ring-number, obj[18]: ring-type, obj[19]: spore-print-color, obj[20]: population, obj[21]: habitat
   # {"feature": "odor", "instances": 8416, "metric_value": 0.9968, "depth": 1}
   if obj[4] == 'NONE':
      # {"feature": "spore-print-color", "instances": 3808, "metric_value": 0.2019, "depth": 2}
      if obj[19] == 'BROWN':
         return 'EDIBLE'
      elif obj[19] == 'BLACK':
         return 'EDIBLE'
      elif obj[19] == 'WHITE':
         # {"feature": "veil-color", "instances": 648, "metric_value": 0.3809, "depth": 3}
         if obj[16] == 'WHITE':
            # {"feature": "gill-size", "instances": 640, "metric_value": 0.3373, "depth": 4}
            if obj[7] == 'BROAD':
               return 'EDIBLE'
            elif obj[7] == 'NARROW':
               # {"feature": "gill-spacing", "instances": 112, "metric_value": 0.9403, "depth": 5}
               if obj[6] == 'CROWDED':
                  # {"feature": "bruises", "instances": 80, "metric_value": 0.469, "depth": 6}
                  if obj[3] == 'NO':
                     return 'EDIBLE'
                  elif obj[3] == 'BRUISES':
                     return 'POISONOUS'
                  else:
                     return 'POISONOUS'
               elif obj[6] == 'CLOSE':
                  return 'POISONOUS'
               else:
                  return 'POISONOUS'
            else:
               return 'EDIBLE'
         elif obj[16] == 'YELLOW':
            return 'POISONOUS'
         else:
            return 'POISONOUS'
      elif obj[19] == 'GREEN':
         return 'POISONOUS'
      elif obj[19] == 'BUFF':
         return 'EDIBLE'
      elif obj[19] == 'YELLOW':
         return 'EDIBLE'
      elif obj[19] == 'ORANGE':
         return 'EDIBLE'
      elif obj[19] == 'CHOCOLATE':
         return 'EDIBLE'
      else:
         return 'EDIBLE'
   elif obj[4] == 'FOUL':
      return 'POISONOUS'
   elif obj[4] == 'SPICY':
      return 'POISONOUS'
   elif obj[4] == 'FISHY':
      return 'POISONOUS'
   elif obj[4] == 'ALMOND':
      return 'EDIBLE'
   elif obj[4] == 'ANISE':
      return 'EDIBLE'
   elif obj[4] == 'PUNGENT':
      return 'POISONOUS'
   elif obj[4] == 'CREOSOTE':
      return 'POISONOUS'
   elif obj[4] == 'MUSTY':
      return 'POISONOUS'
   else:
      return 'POISONOUS'
