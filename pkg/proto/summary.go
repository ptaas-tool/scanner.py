package proto

type (
    Summary struct {
        Negative Section `json:"negative"`
        Positive Section `json:"positive"`
    }

    Section struct {
        Score      int            `json:"score"`
        Total      int            `json:"total_sent"`
        Resolved   int            `json:"resolved_tests"`
        Blocked    int            `json:"blocked_tests"`
        Bypassed   int            `json:"bypassed_tests"`
        Unresolved int            `json:"unresolved_tests"`
        Failed     int            `json:"failed_tests"`
        Tests      map[string]Set `json:"test_sets"`
    }

    Set map[string]Item

    Item struct {
        Percentage float64 `json:"percentage"`
        Sent       int     `json:"sent"`
        Blocked    int     `json:"blocked"`
        Bypassed   int     `json:"bypassed`
        Unresolved int     `json:"unresolved"`
        Failed     int     `json:"failed"`
    }
)
