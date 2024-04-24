import matplotlib.pyplot as plt
import japanize_matplotlib

def table_img(data):
  col = ['1限','2限','3限','4限','5限','1限','2限','3限','4限','5限']
  for i in range(10):
    data[i].insert(0, col[i])

  # 第1ターム
  plt.figure(figsize=(6,2))
  plt.axis('off')

  table1 = plt.table(
          cellText=data[:5], 
          colLabels=['第1ターム', '月曜', '火曜', '水曜', '木曜', '金曜'], 
          loc='center'
  )

  plt.savefig('schedules1.png', dpi=200)

  # 第2ターム
  plt.clf()
  plt.figure(figsize=(6,2))
  plt.axis('off')

  table2 = plt.table(
          cellText=data[5:], 
          colLabels=['第2ターム', '月曜', '火曜', '水曜', '木曜', '金曜'], 
          loc='center'
  )
  plt.savefig('schedules2.png', dpi=200)