# Data Model: Todo In-Memory Console App

## Task Entity

### Fields
- **id**: integer (auto-increment, unique)
  - Validation: Required, positive integer
  - State: Generated automatically, immutable after creation
  
- **title**: string (required)
  - Validation: Required, non-empty string
  - State: Modifiable
  
- **description**: string (optional)
  - Validation: Optional, can be empty string
  - State: Modifiable
  
- **completed**: boolean (default: false)
  - Validation: Boolean value
  - State: Modifiable (via toggle operation)
  
- **priority**: string (Low | Medium | High)
  - Validation: Required, one of the three values
  - State: Modifiable
  
- **category**: string (default: "General")
  - Validation: Optional, defaults to "General"
  - State: Modifiable

### Relationships
- No relationships with other entities (standalone entity)

### State Transitions
- **completed**: Can transition between true and false states (toggle operation)

### Validation Rules
- title must not be empty
- priority must be one of: "Low", "Medium", "High"
- id must be unique within the application session
- id must be a positive integer

### Default Values
- completed: false
- category: "General"