# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:29:33 2021

@author: ninad
"""

import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-STQREDO;'
                      'Database=AdventureWorks2017;'
                      'Trusted_Connection=yes;')

query = "SELECT [CardType], [SubTotal], [TotalDue] FROM AdventureWorks2017.Sales.SalesOrderHeader inner join Sales.CreditCard on CreditCard.CreditCardID = Sales.SalesOrderHeader.CreditCardID"

df = pd.read_sql_query(query,conn)
