package proto

type (
    Summary struct {
        Negative Section `json:"negative"`
        Positive Section `json:"positive"`
    }

    Section struct {
        Score      int    `json:"score"`
        Total      int    `json:"total_sent"`
        Resolved   int    `json:"resolved_tests"`
        Blocked    int    `json:"blocked_tests"`
        Bypassed   int    `json:"bypassed_tests"`
        Unresolved int    `json:"unresolved_tests"`
        Failed     int    `json:"failed_tests"`
        Tests      string `json:"test_sets"`
    }
)
