from pydantic import BaseModel


class QueueMessageFlatFiles(BaseModel):
    model_id: str
    reference_data_path: str
    current_data_path: str
