import os

from django.http import HttpResponse
from dotenv import load_dotenv
from llama_index import load_index_from_storage
from llama_index import QuestionAnswerPrompt
from llama_index import StorageContext


def ask(request):
    """ """
    query_str = request.POST.get("question")

    if not query_str:
        return HttpResponse("Please provide a question.", status=200)

    load_dotenv()
    os.environ.get("OPENAI_API_KEY")
    # index_file_path = os.path.join(
    #     settings.BASE_DIR, "indexed_questions", "django_custom_user_model.json"
    # )
    storage_context = StorageContext.from_defaults(persist_dir="data")
    index = load_index_from_storage(
        storage_context, index_id="django_custom_user_model.json"
    )
    # index = GPTVectorStoreIndex.load_from_disk(index_file_path)
    qa_prompt_tmpl = (
        "Hello, I have some context information for you:\n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Based on this context, could you please help me understand the answer to this question: {query_str}?\n"
    )
    qa_prompt = QuestionAnswerPrompt(qa_prompt_tmpl)

    query_engine = index.as_query_engine(text_qa_template=qa_prompt)
    answer = query_engine.query(query_str)

    return HttpResponse(answer, status=200)
