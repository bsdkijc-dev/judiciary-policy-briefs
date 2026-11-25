# Normalization Rules

1. **Numeric Formatting**: Indonesian dot-separated thousands (`38.148`, `2.937.634`) are normalized to pure integers (`38148`, `2937634`). Comma-separated decimals (`99,54%`) are normalized to standard floats (`99.54`) without `%` signs.
2. **Court Identifiers**: Standardized `court_id` codes map institutional tiers consistently:
   - `MA-RI`: Mahkamah Agung Republik Indonesia (Supreme Court)
   - `NAT-ALL`: Mahkamah Agung + Subordinate Courts (All Tiers)
   - `NAT-4J`: 4 Subordinate Judicial Environments (General, Religious, Military, State Administrative)
   - `APP-4J` / `APP-ALL`: Appellate Courts
   - `FIRST-4J` / `FIRST-ALL`: First Instance Courts
   - `TAX-CT`: Tax Court (*Pengadilan Pajak*)
3. **Indicator Separation**: Both `deciding_productivity_rate`, `official_clearance_rate`, and `standard_clearance_rate` are stored in separate columns so Indonesian and international definitions are never conflated.
