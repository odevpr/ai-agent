get_company_profile_tool = {
  "type": "function",
  "function": {
    "name": "get_company_profile",
    "description": "Retrieve and format a detailed profile of a company using its stock ticker symbol.",
    "parameters": {
      "type": "object",
      "properties": {
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        }
      },
      "required": ["symbol"]
    }
  }
}

get_company_news_tool = {
  "type": "function",
  "function": {
    "name": "get_company_news",
    "description": "Fetch recent news articles about a company based on its stock ticker, within a specified date range.",
    "parameters": {
      "type": "object",
      "properties": {
        "entity": {
          "type": "string",
          "description": "entity type: company"
        },
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        },
        "start_date": {
          "type": "string",
          "description": "start date of the search period for the company's basic financials, yyyy-mm-dd"
        },
        "end_date": {
          "type": "string",
          "description": "end date of the search period for the company's basic financials, yyyy-mm-dd"
        },
        "max_news_num": {
          "type": "integer",
          "description": "maximum number of news to return, default to 10"
        }
      },
      "required": ["entity", "symbol", "start_date", "end_date"]
    }
  }
}

get_basic_financials_history_tool = {
  "type": "function",
  "function": {
    "name": "get_basic_financials_history",
    "description": "Retrieve historical financial data for a company, specified by stock ticker, for chosen financial metrics over time.",
    "parameters": {
      "type": "object",
      "properties": {
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        },
        "freq": {
          "type": "string",
          "description": "reporting frequency of the company's basic financials: annual / quarterly"
        },
        "start_date": {
          "type": "string",
          "description": "start date of the search period for the company's basic financials, yyyy-mm-dd"
        },
        "end_date": {
          "type": "string",
          "description": "end date of the search period for the company's basic financials, yyyy-mm-dd"
        },
        "selected_columns": {
          "type": "array",
          "description": "List of column names of news to return, should be chosen from 'assetTurnoverTTM', 'bookValue', 'cashRatio', 'currentRatio', 'ebitPerShare', 'eps', 'ev', 'fcfMargin', 'fcfPerShareTTM', 'grossMargin', 'inventoryTurnoverTTM', 'longtermDebtTotalAsset', 'longtermDebtTotalCapital', 'longtermDebtTotalEquity', 'netDebtToTotalCapital', 'netDebtToTotalEquity', 'netMargin', 'operatingMargin', 'payoutRatioTTM', 'pb', 'peTTM', 'pfcfTTM', 'pretaxMargin', 'psTTM', 'ptbv', 'quickRatio', 'receivablesTurnoverTTM', 'roaTTM', 'roeTTM', 'roicTTM', 'rotcTTM', 'salesPerShare', 'sgaToSale', 'tangibleBookValue', 'totalDebtToEquity', 'totalDebtToTotalAsset', 'totalDebtToTotalCapital', 'totalRatio'",
          "items": {
            "type": "string"
          }
        }
      },
      "required": ["symbol", "freq"]
    }
  }
}

get_basic_financials_tool = {
  "type": "function",
  "function": {
    "name": "get_basic_financials",
    "description": "Get the most recent basic financial data for a company using its stock ticker symbol, with optional specific financial metrics.",
    "parameters": {
      "type": "object",
      "properties": {
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        },
        "selected_columns": {
          "type": "array",
          "description": "List of column names of news to return, should be chosen from a comprehensive list of financial metrics.",
          "items": {
            "type": "string"
          }
        }
      },
      "required": ["symbol"]
    }
  }
}


get_sec_filing_tool = {
  "type": "function",
  "function": {
    "name": "get_sec_filing",
    "description": "Obtain the most recent SEC filing for a company specified by its stock ticker, within a given date range.",
    "parameters": {
      "type": "object",
      "properties": {
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        },
        "form": {
          "type": "string",
          "description": "Form type from the list: '10-K', '10-Q', '8-K', etc.",
          "default": "10-K"
        },
        "from_date": {
          "type": "string",
          "description": "From date, format yyyy-mm-dd",
          "default": "today(12)"
        },
        "to_date": {
          "type": "string",
          "description": "To date, format yyyy-mm-dd",
          "default": "today()"
        }
      },
      "required": ["symbol"]
    }
  }
}

get_income_stmt_tool = {
  "type": "function",
  "function": {
    "name": "get_income_stmt",
    "description": "Retrieve the latest income statement for the stock defined by the initialized ticker symbol.",
    "parameters": {
      "type": "object",
      "properties": {
        "symbol": {
          "type": "string",
          "description": "ticker symbol"
        }
      },
      "required": ["symbol"]
    }
  }
}

get_10k_section_tool = {
  "type": "function",
  "function": {
    "name": "get_10k_section",
    "description": "Get a specific section of a 10-K report from the SEC API.",
    "parameters": {
      "type": "object",
      "properties": {
        "ticker_symbol": {
          "type": "string",
          "description": "ticker symbol"
        },
        "fyear": {
          "type": "string",
          "description": "fiscal year of the 10-K report"
        },
        "section": {
          "type": "string",
          "description": "Section of the 10-K report to extract, should be in [1, 1A, 1B, 2, 3, 4, 5, 6, 7, 7A, 8, 9, 9A, 9B, 10, 11, 12, 13, 14, 15]"
        },
        "report_address": {
          "type": "string",
          "description": "URL of the 10-K report, if not specified, will get report url from fmp api",
        }
      },
      "required": ["ticker_symbol", "fyear", "section"]
    }
  }
}
