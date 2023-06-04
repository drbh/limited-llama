type Digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" | "13";
type Operator = "+" | "-" | "*" | "/";
type Result = {
    "thought": [Digit, Operator, Digit, "=", "@"],
    "left": ["@", Digit, Digit],
    "unused": [Digit, Digit],
};