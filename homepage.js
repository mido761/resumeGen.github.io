import { HfInference } from '@huggingface/inference';
import dotenv from 'dotenv';
dotenv.config()
const inference = new HfInference(process.env.HUGGING_FACE_API_KEY);
let output = ""

let result = ""

let input = ""
export const fetchInference = async function (inputElem ,outputElem, AssistantMessage) {
    try {
        outputElem = ''; // Clear previous 
        input = inputElem + "\n" + AssistantMessage 
        console.log("the user message is: " + input)
        for await (const chunk of inference.chatCompletionStream({
            model: "tiiuae/falcon-7b-instruct",
            messages: [{ role: "user", content: input}],
            max_tokens: 95,
        })) {
            output = chunk.choices[0]?.delta?.content || "";
            outputElem += output.replace("User", "").replace(" summary", "").replace(":", "").replace(/[\r\n]+/g, '');
            
        }
        return outputElem

    } catch (error) {
        console.error("Error during inference:", error);
        outputElem = "Error occurred during inference.";
    }
}


