# Vendor Performance Analysis

## Business Overview

This project analyzes end-to-end vendor performance by integrating procurement, inventory, sales, and pricing data into a unified analytical dataset. The objective is to identify cost optimization opportunities, improve inventory utilization, evaluate supplier performance, and support data-driven procurement decisions.

---

## Business Objectives

- Evaluate vendor contribution to overall sales and profitability.
- Identify high-value and underperforming vendors.
- Optimize procurement costs through bulk purchasing analysis.
- Improve inventory turnover and reduce excess stock.
- Measure profit margins across vendors and brands.
- Minimize supplier dependency and procurement risk.

---

## Data Model

The project integrates multiple business tables into a single analytical dataset.

```text
                 Vendors
                    │
             Vendor Number
                    │
        ┌───────────┼───────────┐
        │                       │
   Purchases             Purchase Prices
        │                       │
        └───────────┬───────────┘
                    │
              Inventory
                    │
                    ▼
                 Sales
                    │
                    ▼
        vendor_sales_summary
```

The `vendor_sales_summary` table serves as the analytical layer by combining procurement, sales, inventory, and pricing information to support business reporting.

---

## Business Workflow

```text
Raw Business Data
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Data Integration
        │
        ▼
Feature Engineering
        │
        ▼
Vendor Performance Analysis
        │
        ▼
Business Insights & Recommendations
```

---

## Key Business Metrics

- Total Purchase Cost
- Total Sales
- Gross Profit
- Profit Margin (%)
- Inventory Value
- Stock Turnover
- Vendor Contribution
- Purchase Quantity
- Unsold Inventory
- Bulk Purchase Savings

---

## Business Insights

### Vendor Performance

- Identified vendors contributing the highest revenue and profitability.
- Segmented vendors based on sales, purchase value, and operational efficiency.
- Highlighted low-performing vendors requiring strategic review.

**Business Value**

- Focus procurement on high-performing suppliers.
- Improve supplier negotiation strategy.
- Reduce dependency on low-value vendors.

---

### Procurement Analysis

- Compared purchase volumes with procurement costs.
- Evaluated benefits of bulk purchasing.
- Identified opportunities to reduce average procurement cost.

**Expected Impact**

- 5–10% reduction in procurement cost.
- Improved supplier contract negotiations.

---

### Inventory Analysis

- Measured inventory holding against sales performance.
- Identified slow-moving inventory and excess stock.
- Estimated capital locked in unsold products.

**Expected Impact**

- Reduce inventory carrying cost.
- Improve working capital utilization.
- Increase inventory turnover.

---

### Profitability Analysis

- Compared gross profit across vendors and brands.
- Identified high-margin products with lower sales potential.
- Highlighted products suitable for promotional campaigns.

**Expected Impact**

- Higher revenue from profitable products.
- Improved overall gross margin.

---

### Supplier Risk Analysis

- Measured vendor concentration using procurement contribution.
- Identified dependency on a limited number of suppliers.

**Expected Impact**

- Lower supply chain risk.
- Improved business continuity.
- Better sourcing diversification.

---

## Business Recommendations

| Recommendation | Business Impact |
|---------------|-----------------|
| Prioritize high-performing vendors | Increase procurement efficiency |
| Expand bulk purchasing for fast-moving products | Lower procurement cost |
| Reduce purchases of slow-moving inventory | Free working capital |
| Promote high-margin products | Increase profitability |
| Diversify supplier base | Reduce procurement risk |
| Track vendor KPIs regularly | Improve supplier performance |

---

## Business Outcome

The analysis transforms raw procurement and sales data into actionable business intelligence that enables organizations to:

- Make data-driven vendor selection decisions.
- Reduce procurement and inventory costs.
- Improve supplier performance management.
- Increase profitability through optimized purchasing.
- Support strategic sourcing and inventory planning.

---

## Tech Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook
