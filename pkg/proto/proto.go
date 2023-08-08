package proto

type Proto struct {
    Date    string  `json:"date"`
    Name    string  `json:"project_name"`
    URL     string  `json:"url"`
    Score   int     `json:"score"`
    FP      string  `json:"fp"`
    Args    string  `json:"args"`
    Summary Summary `json:"summary"`
}
