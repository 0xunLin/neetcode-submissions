impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();

        for token in tokens {
            match token.as_str() {
                "+" => {
                    let num1 = stack.pop().unwrap();
                    let num2 = stack.pop().unwrap();

                    stack.push(num2+num1);
                }
                "-" => {
                    let num1 = stack.pop().unwrap();
                    let num2 = stack.pop().unwrap();

                    stack.push(num2-num1);
                }
                "*" => {
                    let num1 = stack.pop().unwrap();
                    let num2 = stack.pop().unwrap();

                    stack.push(num2*num1);
                }
                "/" => {
                    let num1 = stack.pop().unwrap();
                    let num2 = stack.pop().unwrap();

                    stack.push(num2/num1);
                }

                _ => {
                    let num = token.parse().unwrap();
                    stack.push(num);
                }
            }
        }

        stack.pop().unwrap()
    }
}
