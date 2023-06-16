import json
import openai
import yaml

openai.api_key = "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"

def get_llm_response():
    with open("prompt.yaml", "r") as f:
        prompt = yaml.safe_load(f)

    with open("scene2.yaml", "r") as f:
        scene = yaml.safe_load(f)

    prompt["messages"].append({"role": "user", "content": json.dumps(scene)})

    response = openai.ChatCompletion.create(model = prompt['model'], messages = prompt['messages'], temperature = prompt['temperature'],)
    print(response)

get_llm_response()

# def get_llm_response(prompt_dir, scene, action_type, scene_dir=None, output_dir=None, loading_cached=False):
#     llm = OpenAI(openai_api_key="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", temperature=0.9, model = 'gpt-4')

#     if loading_cached:
#         with open(f"{output_dir}/action_proposal.yaml", "r") as f:
#             action_proposal = yaml.safe_load(f)

#         action_list = parse_response(action_type, action_proposal)
#         return action_list

#     prompt = load_prompt(prompt_dir)

#     if scene_dir is not None:
#         scene = load_yaml(scene_dir)

#     prompt["messages"].append({
#             "role": "user",
#             "content": json.dumps(scene)
#         })

#     response = llm.ChatCompletion.create(
#             model = prompt["model"],
#             messages = prompt["messages"],
#             temperature = prompt["temperature"],
#     )
#     usage = response['usage']['total_tokens']
#     action_proposal = response['choices'][0]['message']['content']

#     action_proposal = yaml.safe_load(action_proposal)
#     # Print or save response
#     if output_dir is not None:
#         with open(f"{output_dir}/action_proposal.yaml", "w") as f:
#             yaml.dump(action_proposal, f)
#     else:
#         print(response)
#         print(f"Total Usage Tokens  {usage}")

#     action_list = parse_response(action_type, action_proposal)

#     return action_list
