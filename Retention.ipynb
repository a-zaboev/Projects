{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Напишем инструмент для рассчёта метрики Retention за разные периоды времени на примере набора данных об активности пользователей в игровом приложении"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import seaborn as sns\n",
    "\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Посмотрим на данные"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>reg_ts</th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>911382223</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>932683089</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>947802447</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>959523541</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>969103313</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      reg_ts  uid\n",
       "0  911382223    1\n",
       "1  932683089    2\n",
       "2  947802447    3\n",
       "3  959523541    4\n",
       "4  969103313    5"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data = pd.read_csv('~/shared/problem1-reg_data.csv', sep = ';')\n",
    "reg_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>reg_ts</th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>999995</th>\n",
       "      <td>1600874034</td>\n",
       "      <td>1110618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999996</th>\n",
       "      <td>1600874086</td>\n",
       "      <td>1110619</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999997</th>\n",
       "      <td>1600874139</td>\n",
       "      <td>1110620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999998</th>\n",
       "      <td>1600874191</td>\n",
       "      <td>1110621</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999999</th>\n",
       "      <td>1600874244</td>\n",
       "      <td>1110622</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            reg_ts      uid\n",
       "999995  1600874034  1110618\n",
       "999996  1600874086  1110619\n",
       "999997  1600874139  1110620\n",
       "999998  1600874191  1110621\n",
       "999999  1600874244  1110622"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "reg_ts    int64\n",
       "uid       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data['uid'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "999995    1110618\n",
       "999996    1110619\n",
       "999997    1110620\n",
       "999998    1110621\n",
       "999999    1110622\n",
       "Name: uid, dtype: int64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data['uid'].sort_values().tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- ID начинаются с первых цифр (1, 2, 3 и т. д). Уникальных - 1 млн, как и строк, при этом если поставить по порядку (а датасет изначально представлен по порядку), то видим, что последние числа- больше миллиона, значит какие-то числа в этом миллионе значений отсутствуют."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Переведём данные во временной колонке из таймстемпа в формат даты:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "reg_data['reg_ts'] = pd.to_datetime(reg_data['reg_ts'], unit='s').dt.date #оставим даты по дням"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "reg_data = reg_data.rename(columns = {'reg_ts' : 'reg_date'}) #переимнуем стобец осознанно"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "reg_date    object\n",
       "uid          int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.dtypes #у даты тип данных obj, надо переделать в datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "reg_data['reg_date'] = pd.to_datetime(reg_data['reg_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Проверим какие года есть  в данных:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,\n",
       "       2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,\n",
       "       2020])"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data['reg_date'].dt.year.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- аж 22 года без пропуска"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>reg_date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1998</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1999</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2000</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2001</th>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2002</th>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2003</th>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2004</th>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2005</th>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2006</th>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2007</th>\n",
       "      <td>216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2008</th>\n",
       "      <td>394</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2009</th>\n",
       "      <td>718</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2010</th>\n",
       "      <td>1308</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2011</th>\n",
       "      <td>2385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012</th>\n",
       "      <td>4361</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013</th>\n",
       "      <td>7932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014</th>\n",
       "      <td>14455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015</th>\n",
       "      <td>26344</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016</th>\n",
       "      <td>48187</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017</th>\n",
       "      <td>87645</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018</th>\n",
       "      <td>159729</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019</th>\n",
       "      <td>291102</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020</th>\n",
       "      <td>354963</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             uid\n",
       "reg_date        \n",
       "1998           1\n",
       "1999           1\n",
       "2000           4\n",
       "2001           6\n",
       "2002          10\n",
       "2003          20\n",
       "2004          35\n",
       "2005          65\n",
       "2006         119\n",
       "2007         216\n",
       "2008         394\n",
       "2009         718\n",
       "2010        1308\n",
       "2011        2385\n",
       "2012        4361\n",
       "2013        7932\n",
       "2014       14455\n",
       "2015       26344\n",
       "2016       48187\n",
       "2017       87645\n",
       "2018      159729\n",
       "2019      291102\n",
       "2020      354963"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.groupby(reg_data['reg_date'].dt.year).agg({\"uid\":\"count\"})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- ежегодно в 1,5-2 раза возрастало количество вновь зарегистрированных юзеров (в основном в - 1,8 раз, а 2020 год наверное ещё не весь прошёл на момент выгрузки)\n",
    "- прогресс замечательный - от единичных пользователей добрались до сотен тысяч"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "reg_date  uid  \n",
       "False     False    1000000\n",
       "dtype: int64"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.isna().value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- пустых значений нет"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Теперь глянем на второй датафрейм и приведём его в такой же порядок"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>auth_ts</th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>911382223</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>932683089</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>932921206</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>933393015</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>933875379</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     auth_ts  uid\n",
       "0  911382223    1\n",
       "1  932683089    2\n",
       "2  932921206    2\n",
       "3  933393015    2\n",
       "4  933875379    2"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "auth_data = pd.read_csv('~/shared/problem1-auth_data.csv', sep = \";\")\n",
    "auth_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9601013, 2)"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "auth_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 9601013 entries, 0 to 9601012\n",
      "Data columns (total 2 columns):\n",
      " #   Column   Dtype\n",
      "---  ------   -----\n",
      " 0   auth_ts  int64\n",
      " 1   uid      int64\n",
      "dtypes: int64(2)\n",
      "memory usage: 146.5 MB\n"
     ]
    }
   ],
   "source": [
    "auth_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth_data['auth_ts'] = pd.to_datetime(auth_data['auth_ts'], unit='s').dt.date\n",
    "auth_data = auth_data.rename(columns = {'auth_ts' : 'auth_date'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth_data['auth_date'] = pd.to_datetime(auth_data['auth_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Проверим уникальных пользователей и пустые значения"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "auth_date  uid  \n",
       "False      False    9601013\n",
       "dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "auth_data.isna().value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000000"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "auth_data['uid'].nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- ничего не потерялось, уникальных пользователей столько же, сколько и в регистрациях.\n",
    "- пустых значений нет"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Посмотрим, сколько активностей отмечается у пользователей в течение жизни в приложении (помимо регистрации):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>activity</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>uid</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>191</th>\n",
       "      <td>1296</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>176</th>\n",
       "      <td>1331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>158</th>\n",
       "      <td>1367</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>1397</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1929</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     activity\n",
       "uid          \n",
       "191      1296\n",
       "176      1331\n",
       "158      1367\n",
       "108      1397\n",
       "2        1929"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "activity = auth_data.groupby('uid').agg({'uid':'count'}).rename(columns = {'uid' : 'activity'}).sort_values(by = 'activity')\n",
    "activity.tail() #группируем по пользователям, считаем их авторизации, сортируем и смотрим на самые большие значения."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "761622"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "activity.query('activity == 1').activity.count() #считаем, сколько пользователей имеют лишь один вход"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    238378.000000\n",
       "mean         37.081404\n",
       "std          91.119322\n",
       "min           2.000000\n",
       "25%           4.000000\n",
       "50%           8.000000\n",
       "75%          11.000000\n",
       "max        1929.000000\n",
       "Name: activity, dtype: float64"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "activity.sort_values(by = 'activity').query('activity > 1').activity.describe() \n",
    "#так как большинство пользователей авторизовывались лишь 1 раз, то смотрим на процентили и пиковые значения, тех, \n",
    "#у кого активность больше 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7ff2e85fd518>"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=activity.query('activity > 11')) \n",
    "#график распределения тех, у кого более 11 авторизаций (75 процентиль)\n",
    "#делаем так, потому что абсолютное большинство значений гораздо меньше и распределение не было бы понятным"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7ff2da087eb8>"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lineplot(data=auth_data.groupby(auth_data.auth_date.dt.year) \\\n",
    "             .agg({'uid':\"count\"}).reset_index(), x='auth_date', y = 'uid')\n",
    "#чем позже дата, тем больше уникальных пользователей (прирост отмечен ранее)\n",
    "#по оси Y количество авторизаций за год в сотнях тысяч, оно растёт пропорционально появлению пользователей,\n",
    "#к концу периода достигая более, чем 300 тыс."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- получается, что активность пользователей бывает переваливала и за 1000 авторизаций, у рекордсмена почти 2 тысячи\n",
    "- у абсолютного большинства пользователей авторизация после регистрации лишь одна\n",
    "- из тех, у кого не одна, в подавляющем большинстве (75%) авторизовывались 11 раз или меньше.\n",
    "- в распределении оставшихся авторизаций (у кого больше 11 раз) аномалий нет, плавное распределение. Больше тех пользователей, которые заходят реже. Где-то после 900 авторизаций начинаются выбросы - единичные случаи диких фанатов. \n",
    "- где-то с 2012 года активность и число юзеров начинают неуклонно расти, есть смысл хорошо проанализировать этот период"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Посмотрим на когорты и попробуем построить таблицу retention"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>reg_date</th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5105</th>\n",
       "      <td>2020-09-19</td>\n",
       "      <td>1634</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5106</th>\n",
       "      <td>2020-09-20</td>\n",
       "      <td>1636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5107</th>\n",
       "      <td>2020-09-21</td>\n",
       "      <td>1638</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5108</th>\n",
       "      <td>2020-09-22</td>\n",
       "      <td>1641</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5109</th>\n",
       "      <td>2020-09-23</td>\n",
       "      <td>1048</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        reg_date   uid\n",
       "5105  2020-09-19  1634\n",
       "5106  2020-09-20  1636\n",
       "5107  2020-09-21  1638\n",
       "5108  2020-09-22  1641\n",
       "5109  2020-09-23  1048"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.groupby(reg_data['reg_date'].dt.date, as_index=True).agg({\"uid\":\"count\"}).reset_index().tail()\n",
    "#группировка по дням регистрации и подсчёт пользователей в них (каждый день прибывает по чутьчуть)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7ff2e85ff7f0>"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lineplot(data=reg_data.groupby(reg_data['reg_date'].dt.date, as_index=True).agg({\"uid\":\"count\"}) \\\n",
    "             .reset_index(), x='reg_date', y = 'uid')\n",
    "#строим график с группировкой по дате регистрации по датам, считаем, сколько пользователей в какие года регистрировались."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>uid</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>5110.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>195.694716</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>350.002960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>201.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1641.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               uid\n",
       "count  5110.000000\n",
       "mean    195.694716\n",
       "std     350.002960\n",
       "min       1.000000\n",
       "25%       3.000000\n",
       "50%      25.000000\n",
       "75%     201.000000\n",
       "max    1641.000000"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg_data.groupby(reg_data['reg_date'].dt.date, as_index=True).agg({\"uid\":\"count\"}).reset_index().describe()\n",
    "#смотрим описание данных пользователей, сгруппированных по дням регистрации"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- у нас всего есть 5110 когорт\n",
    "- четверть из них - совсем маленькие - до 3 человек\n",
    "- есть более, чем полуторатысячные дни прихода новых пользователей\n",
    "- похоже, что ежедневно (кроме того, что и ежегодно) всё больше и больше пользователей увлекается нашим сервисом \n",
    "- на момент выгрузки данные не за весь 2020 год"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Построим таблицу retention на базе небольшого диапазона - 20 дней одного месяца (но уже жаркого 2019 года)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>day</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>10</th>\n",
       "      <th>11</th>\n",
       "      <th>12</th>\n",
       "      <th>13</th>\n",
       "      <th>14</th>\n",
       "      <th>15</th>\n",
       "      <th>16</th>\n",
       "      <th>17</th>\n",
       "      <th>18</th>\n",
       "      <th>19</th>\n",
       "      <th>20</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>reg_date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-01</th>\n",
       "      <td>583.0</td>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "      <td>29</td>\n",
       "      <td>26</td>\n",
       "      <td>37</td>\n",
       "      <td>48</td>\n",
       "      <td>34</td>\n",
       "      <td>32</td>\n",
       "      <td>35</td>\n",
       "      <td>35</td>\n",
       "      <td>27</td>\n",
       "      <td>33</td>\n",
       "      <td>20</td>\n",
       "      <td>28</td>\n",
       "      <td>27</td>\n",
       "      <td>33</td>\n",
       "      <td>28</td>\n",
       "      <td>23</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-02</th>\n",
       "      <td>583.0</td>\n",
       "      <td>10</td>\n",
       "      <td>29</td>\n",
       "      <td>21</td>\n",
       "      <td>29</td>\n",
       "      <td>47</td>\n",
       "      <td>32</td>\n",
       "      <td>41</td>\n",
       "      <td>18</td>\n",
       "      <td>24</td>\n",
       "      <td>25</td>\n",
       "      <td>34</td>\n",
       "      <td>32</td>\n",
       "      <td>29</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>16</td>\n",
       "      <td>28</td>\n",
       "      <td>29</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-03</th>\n",
       "      <td>585.0</td>\n",
       "      <td>10</td>\n",
       "      <td>18</td>\n",
       "      <td>26</td>\n",
       "      <td>35</td>\n",
       "      <td>37</td>\n",
       "      <td>38</td>\n",
       "      <td>34</td>\n",
       "      <td>13</td>\n",
       "      <td>29</td>\n",
       "      <td>28</td>\n",
       "      <td>40</td>\n",
       "      <td>20</td>\n",
       "      <td>27</td>\n",
       "      <td>23</td>\n",
       "      <td>29</td>\n",
       "      <td>25</td>\n",
       "      <td>26</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-04</th>\n",
       "      <td>585.0</td>\n",
       "      <td>16</td>\n",
       "      <td>22</td>\n",
       "      <td>25</td>\n",
       "      <td>32</td>\n",
       "      <td>32</td>\n",
       "      <td>47</td>\n",
       "      <td>31</td>\n",
       "      <td>25</td>\n",
       "      <td>31</td>\n",
       "      <td>33</td>\n",
       "      <td>38</td>\n",
       "      <td>35</td>\n",
       "      <td>24</td>\n",
       "      <td>24</td>\n",
       "      <td>33</td>\n",
       "      <td>23</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-05</th>\n",
       "      <td>586.0</td>\n",
       "      <td>11</td>\n",
       "      <td>24</td>\n",
       "      <td>27</td>\n",
       "      <td>29</td>\n",
       "      <td>48</td>\n",
       "      <td>42</td>\n",
       "      <td>41</td>\n",
       "      <td>35</td>\n",
       "      <td>24</td>\n",
       "      <td>28</td>\n",
       "      <td>38</td>\n",
       "      <td>30</td>\n",
       "      <td>34</td>\n",
       "      <td>31</td>\n",
       "      <td>24</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-06</th>\n",
       "      <td>588.0</td>\n",
       "      <td>10</td>\n",
       "      <td>22</td>\n",
       "      <td>31</td>\n",
       "      <td>28</td>\n",
       "      <td>35</td>\n",
       "      <td>33</td>\n",
       "      <td>34</td>\n",
       "      <td>31</td>\n",
       "      <td>28</td>\n",
       "      <td>30</td>\n",
       "      <td>36</td>\n",
       "      <td>29</td>\n",
       "      <td>23</td>\n",
       "      <td>29</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-07</th>\n",
       "      <td>588.0</td>\n",
       "      <td>10</td>\n",
       "      <td>25</td>\n",
       "      <td>24</td>\n",
       "      <td>32</td>\n",
       "      <td>43</td>\n",
       "      <td>43</td>\n",
       "      <td>39</td>\n",
       "      <td>32</td>\n",
       "      <td>32</td>\n",
       "      <td>20</td>\n",
       "      <td>40</td>\n",
       "      <td>28</td>\n",
       "      <td>31</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-08</th>\n",
       "      <td>589.0</td>\n",
       "      <td>18</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>34</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "      <td>39</td>\n",
       "      <td>34</td>\n",
       "      <td>23</td>\n",
       "      <td>29</td>\n",
       "      <td>31</td>\n",
       "      <td>30</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-09</th>\n",
       "      <td>590.0</td>\n",
       "      <td>6</td>\n",
       "      <td>16</td>\n",
       "      <td>25</td>\n",
       "      <td>31</td>\n",
       "      <td>35</td>\n",
       "      <td>38</td>\n",
       "      <td>26</td>\n",
       "      <td>34</td>\n",
       "      <td>30</td>\n",
       "      <td>26</td>\n",
       "      <td>26</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-10</th>\n",
       "      <td>591.0</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>30</td>\n",
       "      <td>42</td>\n",
       "      <td>28</td>\n",
       "      <td>35</td>\n",
       "      <td>31</td>\n",
       "      <td>40</td>\n",
       "      <td>23</td>\n",
       "      <td>32</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-11</th>\n",
       "      <td>593.0</td>\n",
       "      <td>13</td>\n",
       "      <td>25</td>\n",
       "      <td>30</td>\n",
       "      <td>46</td>\n",
       "      <td>34</td>\n",
       "      <td>45</td>\n",
       "      <td>45</td>\n",
       "      <td>24</td>\n",
       "      <td>25</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-12</th>\n",
       "      <td>593.0</td>\n",
       "      <td>13</td>\n",
       "      <td>22</td>\n",
       "      <td>27</td>\n",
       "      <td>34</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "      <td>41</td>\n",
       "      <td>40</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-13</th>\n",
       "      <td>594.0</td>\n",
       "      <td>15</td>\n",
       "      <td>25</td>\n",
       "      <td>35</td>\n",
       "      <td>29</td>\n",
       "      <td>35</td>\n",
       "      <td>59</td>\n",
       "      <td>49</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-14</th>\n",
       "      <td>595.0</td>\n",
       "      <td>11</td>\n",
       "      <td>24</td>\n",
       "      <td>26</td>\n",
       "      <td>23</td>\n",
       "      <td>42</td>\n",
       "      <td>41</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-15</th>\n",
       "      <td>596.0</td>\n",
       "      <td>9</td>\n",
       "      <td>23</td>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>42</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-16</th>\n",
       "      <td>597.0</td>\n",
       "      <td>12</td>\n",
       "      <td>27</td>\n",
       "      <td>37</td>\n",
       "      <td>40</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-17</th>\n",
       "      <td>598.0</td>\n",
       "      <td>11</td>\n",
       "      <td>25</td>\n",
       "      <td>29</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-18</th>\n",
       "      <td>599.0</td>\n",
       "      <td>8</td>\n",
       "      <td>25</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-19</th>\n",
       "      <td>600.0</td>\n",
       "      <td>5</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-20</th>\n",
       "      <td>601.0</td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "day            1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  \\\n",
       "reg_date                                                                        \n",
       "2019-01-01  583.0  12  22  29  26  37  48  34  32  35  35  27  33  20  28  27   \n",
       "2019-01-02  583.0  10  29  21  29  47  32  41  18  24  25  34  32  29  26  27   \n",
       "2019-01-03  585.0  10  18  26  35  37  38  34  13  29  28  40  20  27  23  29   \n",
       "2019-01-04  585.0  16  22  25  32  32  47  31  25  31  33  38  35  24  24  33   \n",
       "2019-01-05  586.0  11  24  27  29  48  42  41  35  24  28  38  30  34  31  24   \n",
       "2019-01-06  588.0  10  22  31  28  35  33  34  31  28  30  36  29  23  29       \n",
       "2019-01-07  588.0  10  25  24  32  43  43  39  32  32  20  40  28  31           \n",
       "2019-01-08  589.0  18  24  30  34  42  42  39  34  23  29  31  30               \n",
       "2019-01-09  590.0   6  16  25  31  35  38  26  34  30  26  26                   \n",
       "2019-01-10  591.0  18  19  30  42  28  35  31  40  23  32                       \n",
       "2019-01-11  593.0  13  25  30  46  34  45  45  24  25                           \n",
       "2019-01-12  593.0  13  22  27  34  40  38  41  40                               \n",
       "2019-01-13  594.0  15  25  35  29  35  59  49                                   \n",
       "2019-01-14  595.0  11  24  26  23  42  41                                       \n",
       "2019-01-15  596.0   9  23  37  32  42                                           \n",
       "2019-01-16  597.0  12  27  37  40                                               \n",
       "2019-01-17  598.0  11  25  29                                                   \n",
       "2019-01-18  599.0   8  25                                                       \n",
       "2019-01-19  600.0   5                                                           \n",
       "2019-01-20  601.0                                                               \n",
       "\n",
       "day         17  18  19  20  \n",
       "reg_date                    \n",
       "2019-01-01  33  28  23  27  \n",
       "2019-01-02  16  28  29      \n",
       "2019-01-03  25  26          \n",
       "2019-01-04  23              \n",
       "2019-01-05                  \n",
       "2019-01-06                  \n",
       "2019-01-07                  \n",
       "2019-01-08                  \n",
       "2019-01-09                  \n",
       "2019-01-10                  \n",
       "2019-01-11                  \n",
       "2019-01-12                  \n",
       "2019-01-13                  \n",
       "2019-01-14                  \n",
       "2019-01-15                  \n",
       "2019-01-16                  \n",
       "2019-01-17                  \n",
       "2019-01-18                  \n",
       "2019-01-19                  \n",
       "2019-01-20                  "
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#ищем 20-дневный фрагмент дат авторизаций, к нему добавляем фрагмент с нужным диапазоном когорт. \n",
    "#Группируем по когортам и авторизациям внутри когорт, считаем заходы пользователей\n",
    "table = auth_data.query('auth_date >= \"2019-01-01\" and auth_date <= \"2019-01-20\"') \\\n",
    ".merge(reg_data.query('reg_date >= \"2019-01-01\" and reg_date <= \"2019-01-31\"'), on='uid', how=\"right\") \\\n",
    ".groupby(['reg_date', 'auth_date']).agg({\"uid\":\"count\"}).reset_index() \\\n",
    "\n",
    "#создаём новую колонку в получившемся датафрейме, которая ранжирует даты захода по номерам дней, в каждой когорте\n",
    "table['day'] = table.groupby(['reg_date'])['auth_date'].rank(method='dense').astype(int)\n",
    "\n",
    "#Группируем таблицу по когорте и номерам дней в ней, суммируем посчитанные заходы (получая то же их число, что и было). \n",
    "#Разворачиваем таблицу, чтобы индексами стали когорты, а колонками - дни, удаляем пустые значения для красоты и наглядности\n",
    "table.groupby(['reg_date', 'day'], as_index=False).agg({\"uid\":\"sum\"}) \\\n",
    ".pivot(columns = 'day', index='reg_date', values='uid').fillna('')\n",
    "\n",
    "#день регистрации - это день 1 (первый)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- построить таблицу удержания получилось\n",
    "- видно, что с сервисом в этом году всё в порядке, пользователи остаются, некоторые приходят еждневно (строил для ранних лет - там довольно скудные данные)\n",
    "\n",
    "- однако, когорт даже за 1 год очень много, смотреть их на одной такой таблице нереально\n",
    "- также у некоторых когорт бывает очень много дней для анализа - на одной таблице не показать\n",
    "- поэтому (помимо таблицы) нужен инструмент, который покажет сводный retention в конкретных заданных диапазонах по датам \n",
    "- также нужна возможность смотреть конкретные номера дней или диапазонов по номерам дней retention для взятых когорт \n",
    "- когорты пользователей, особенно в последние годы, заходят ежедневно так что надо рассчитать классический ретеншн N-го дня\n",
    "- нам нужно смотреть сводный процент по каждому дню того или иного диапазона когорт, расчитав средневзвешанное значение\n",
    "- отдельной функцией можно в принципе возвращать и саму получившуюся таблицу в абсолютных числах или процентах в заданных интервалах когорт и дней, однако, здесь реализуем именно идею - сделать инструмент для получения сводных процентов за заданный период. Кроме того, с такой таблицей проще будет работать в дальнейшем (графики, перерасчёты)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### На основе построенной таблицы и выводов сделаем нужную функцию "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "На вход будет несколько переменных:\n",
    "- дата старта диапазона и дата его окончания (будут оцениваться все когорты этого периода)\n",
    "- номер начального дня диапазона, и номер конечного дня (чтобы посмотреть ретеншн за опредлённый номер дня, несколько дней или все дни)\n",
    "- датафрейм с регистрациями\n",
    "- датафрейм с активностью\n",
    "\n",
    "(!) Для ускорения обработки данных преобразование дат наших датафреймов оставим за пределами функции (но всегда можем положить и внутрь)\n",
    "Функция будет применяться самостоятельно, а не для какого-либло датафрейма, так как у нас два основополагающих датафрейма (регистрации и авторизации) - к одному из них или к их джойну применять функцию не имеет смысла, сделаем самодостаточную функцию."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- загружаем данные заново и проводим обработку дат за пределами функции:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "reg_data = pd.read_csv('~/shared/problem1-reg_data.csv', sep = ';') \n",
    "\n",
    "reg_data['reg_ts'] = pd.to_datetime(reg_data['reg_ts'], unit='s').dt.date \n",
    "reg_data = reg_data.rename(columns = {'reg_ts' : 'reg_date'})\n",
    "reg_data['reg_date'] = pd.to_datetime(reg_data['reg_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth_data = pd.read_csv('~/shared/problem1-auth_data.csv', sep = \";\") #загружаем данные авторизаций заново\n",
    "\n",
    "auth_data['auth_ts'] = pd.to_datetime(auth_data['auth_ts'], unit='s').dt.date #проводим обработку дат за пределами функции\n",
    "auth_data = auth_data.rename(columns = {'auth_ts' : 'auth_date'})\n",
    "auth_data['auth_date'] = pd.to_datetime(auth_data['auth_date'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- вводим переменные диапазонов когорт:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "date_range_start = f'2013-01-01' #поменяйте дату на нужную для определения начала диапазона\n",
    "\n",
    "date_rage_end = f'2013-12-31' #поменяйте дату на нужную для определения конца диапазона"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- вводим переменные диапазонов нужных для анализа дней:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "day_range_start = f'0' #поменяйте число на нужный номер дня начала диапазона\n",
    "\n",
    "day_range_end = f'100' #поменяйте число на нужный номер дня конца диапазона"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Cоздаём функцию, в которой:\n",
    "  - На вход принимаются датафреймы с регистрациями и авторизациями, диапазон дат, соответствующих когортам, диапазон нужных дней\n",
    "  - Создаём общий датафрейм с нужным диапазоном дат, в нём на каждую авторизацию показан uid пользователя и дата его регистрации\n",
    "  - Создаём колонку с нумерацией дней от дня регистрации - это день 0 (нулевой)\n",
    "  - Считаем в каждой когорте и в каждом номере дня ретеншен в абсолютных числах с помощью группировки и аггрегации\n",
    "  - Создаём колонку в процентах ретеншн по каждому дню в каждой когорте, обращаясь к первому значению в каждой когорте (то есть от размера когорты)\n",
    "  - Создаём колонку, где для каждой строки показываем размер соответствующей ей когорты (количество пользователей на первый день)\n",
    "  - Рассчитываем вес каждого дня в когорте (в принципе это всегда будет абсолютное количество пользователей за день, которое у нас уже имеется, умноженное на 100, но всё рассчитаем для соблюдения порядка в формуле)\n",
    "  - Создаём общий датафрейм для всех когорт нашего диапазона дат и группируем по каждому номеру дня. В аггрегации суммируем веса каждого из дней, а также размеры всех когорт, данные по которым есть для этого дня (согласно формуле вычисления средневзвешнного значения - вклад в вес каждого дня делится на сумму размеров когорт для каждого дня)\n",
    "  - Наконец создаём колонку, в которой делим общий вес дня на общий размер всех когорт для дня, получая показатель удержания пользователей в процентах c округлением\n",
    "  - Возвращаем средневзвешенное значение retention в процентах для всех дней в диапазоне, заданном пользователем\n",
    "\n",
    "(описание будет также в самой функции)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "def retention_per_day(reg_data, auth_data, day_range_start, day_range_end, date_range_start, date_rage_end):\n",
    "    \n",
    "    #общий датафрейм:\n",
    "    df = auth_data \\\n",
    "        .merge(reg_data.query(f'reg_date >= \"{date_range_start}\" and reg_date <= \"{date_rage_end}\"'), on='uid', how=\"right\")\n",
    "    \n",
    "    #нумерация дней от даты регистрации:\n",
    "    df['day'] = (df['auth_date'] - df['reg_date']).dt.days\n",
    "    \n",
    "    #датафрейм по когортам, внутри них каждый день пронумерован, вычислено абсолютное число пришедших пользователей в день:\n",
    "    retention = df.groupby(['reg_date', 'day'], as_index=False).agg({'uid':'count'})\n",
    "    \n",
    "    #осмысленно переименована колонка:\n",
    "    retention = retention.rename(columns = {\"uid\":\"absolut\"})\n",
    "    \n",
    "    #колонка, содержащая процент ретеншн каждого дня от первого значения (от размера когорты):\n",
    "    retention['percent'] = retention.groupby('reg_date', as_index=False)['absolut'].transform(lambda x: x / x.iloc[0] * 100)\n",
    "    \n",
    "    #техническая колонка, показывающая в каждой строке соответствующую ей когорту (её размер): \n",
    "    retention['cohort_size'] = retention.groupby('reg_date', as_index=False)['absolut'].transform(lambda x: x.iloc[0])\n",
    "    \n",
    "    #вес каждого дня в когорте - то есть произведение размера когорты и процента retention:\n",
    "    retention['weight'] = retention['cohort_size'] * retention['percent']\n",
    "\n",
    "    #группировка по дням, вычисление суммы весов и суммы размеров когорт:\n",
    "    retention_per_day = retention.groupby('day', as_index=False).agg({'weight': 'sum', 'cohort_size' : 'sum'})\n",
    "    \n",
    "    #колонка, показывающая средневзвешенное арифметическое для каждого дня диапазона дат в процентах, \n",
    "    #округлённое до 3 знаков после запятой с добавлением символа процентов:\n",
    "    retention_per_day['retention'] = round(retention_per_day['weight'] / retention_per_day['cohort_size'], 2) \\\n",
    "                                    #.apply(lambda x: str(x) + ' %') #при необходимости расчётов с данными, визуализации \n",
    "                                                                    #эту функцию можно вводить или убирать, \n",
    "                                                                    #чтобы тип вернулся к float\n",
    "    \n",
    "    #удаление лишних колонок с весом и размером когорт:\n",
    "    retention_per_day = retention_per_day.drop(columns = ['weight', 'cohort_size']).reset_index(drop=True)\n",
    "    \n",
    "    #функция возвращает средневзвешенное значение retention в процентах для дней в диапазоне, заданном пользователем:\n",
    "    return retention_per_day.query(f'day >= {day_range_start} and day <= {day_range_end}') \\\n",
    "            #.style.hide_index() \\\n",
    "            #.set_caption(f'Retention: days {day_range_start}-{day_range_end}  \\\n",
    "            #for cohorts from {date_range_start} to {date_rage_end}')\n",
    "            #при необходимости расчётов с данными и визуализации можно вводить или убирать подпись к таблице"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style><table id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6\" ><caption>Retention: days 0-20              for cohorts from 2013-01-01 to 2013-12-31</caption><thead>    <tr>        <th class=\"col_heading level0 col0\" >day</th>        <th class=\"col_heading level0 col1\" >retention</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row0_col0\" class=\"data row0 col0\" >0</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row0_col1\" class=\"data row0 col1\" >100.0 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row1_col0\" class=\"data row1 col0\" >1</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row1_col1\" class=\"data row1 col1\" >5.74 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row2_col0\" class=\"data row2 col0\" >2</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row2_col1\" class=\"data row2 col1\" >6.75 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row3_col0\" class=\"data row3 col0\" >3</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row3_col1\" class=\"data row3 col1\" >6.98 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row4_col0\" class=\"data row4 col0\" >4</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row4_col1\" class=\"data row4 col1\" >7.65 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row5_col0\" class=\"data row5 col0\" >5</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row5_col1\" class=\"data row5 col1\" >7.92 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row6_col0\" class=\"data row6 col0\" >6</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row6_col1\" class=\"data row6 col1\" >8.28 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row7_col0\" class=\"data row7 col0\" >7</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row7_col1\" class=\"data row7 col1\" >8.28 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row8_col0\" class=\"data row8 col0\" >8</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row8_col1\" class=\"data row8 col1\" >6.89 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row9_col0\" class=\"data row9 col0\" >9</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row9_col1\" class=\"data row9 col1\" >7.5 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row10_col0\" class=\"data row10 col0\" >10</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row10_col1\" class=\"data row10 col1\" >7.54 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row11_col0\" class=\"data row11 col0\" >11</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row11_col1\" class=\"data row11 col1\" >7.37 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row12_col0\" class=\"data row12 col0\" >12</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row12_col1\" class=\"data row12 col1\" >7.43 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row13_col0\" class=\"data row13 col0\" >13</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row13_col1\" class=\"data row13 col1\" >7.04 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row14_col0\" class=\"data row14 col0\" >14</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row14_col1\" class=\"data row14 col1\" >7.0 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row15_col0\" class=\"data row15 col0\" >15</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row15_col1\" class=\"data row15 col1\" >6.71 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row16_col0\" class=\"data row16 col0\" >16</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row16_col1\" class=\"data row16 col1\" >6.73 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row17_col0\" class=\"data row17 col0\" >17</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row17_col1\" class=\"data row17 col1\" >7.03 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row18_col0\" class=\"data row18 col0\" >18</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row18_col1\" class=\"data row18 col1\" >6.67 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row19_col0\" class=\"data row19 col0\" >19</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row19_col1\" class=\"data row19 col1\" >6.9 %</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row20_col0\" class=\"data row20 col0\" >20</td>\n",
       "                        <td id=\"T_47d023fe_ead1_11ee_bdbb_96000040dfb6row20_col1\" class=\"data row20 col1\" >6.72 %</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x7ff2e85f7b00>"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "retention_per_day(reg_data, auth_data, day_range_start, day_range_end, date_range_start, date_rage_end)\n",
    "#для этого убрали рещётки с закомментированных функций добавления знака процентов и со стилевой подпипи таблицы\n",
    "#ввели переменные с 0 по 20 день ретеншн и когорты за с начала по конец 2013 года"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "#создаём датафрейм по году с помощью нашей фурнкции с нужными вводными (весь 2012 год и 100 дней для каждой когорты)\n",
    "visual_2012 = retention_per_day(reg_data, auth_data, day_range_start, day_range_end, date_range_start, date_rage_end)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "#создаём датафрейм по другому году с помощью нашей фурнкции с новыми вводными (весь 2013 год и 100 дней для каждой когорты)\n",
    "visual_2013 = retention_per_day(reg_data, auth_data, day_range_start, day_range_end, date_range_start, date_rage_end)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#создаём пример визуализации retention на основе датафреймов из нашей функции\n",
    "plt.figure(figsize=(15, 6))\n",
    "\n",
    "plt.xticks(ticks=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])\n",
    "plt.yticks(ticks=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])\n",
    "\n",
    "plt.title(f'Retention 0-100 days for cohorts at 2012 and 2013 years')\n",
    "\n",
    "retention_12 = sns.lineplot(data=visual_2012, y = 'retention', x=\"day\", color = 'red') \n",
    "retention_13 = sns.lineplot(data=visual_2013, y = 'retention', x=\"day\", color = 'blue') \n",
    "\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- полученный с помощью функции датафрейм показывает средневешенное значение в процентах по диапазону когорт\n",
    "- он также может показать данные и по каждой когорте отдельно, если на старте и энде ввести одну и ту же дату\n",
    "- он покажет данные удержания за диапазон дней, за один день или все возможные дни \n",
    "- часть кода можно использовать для получения конкретных абсолютных значений по каждому дню\n",
    "- также по таблице удобно строить график, например если мы берём много дней, что не вмещается на один экран таблицей\n",
    "- сравнивать можно несколько выбранных ретеншенов по когортам или их диапазонам"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Набор данных взят из программы обучения на Аналитика данных  в Karpov Courses"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
