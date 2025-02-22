import os

with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r', encoding='utf-8') as f:
    __version__ = f.read().strip()


from importlib.metadata import version

from openssm.core.prompts import Prompts
from openssm.core.slm.base_slm import BaseSLM
from openssm.core.ssm.base_ssm import BaseSSM

from openssm.integrations.openai.ssm import GPT3CompletionSSM, GPT3ChatCompletionSSM, GPT4ChatCompletionSSM
from openssm.integrations.huggingface.ssm import Falcon7bSSM
from openssm.integrations.llama_index.ssm import SSM as LlamaIndexSSM
from openssm.integrations.llama_index.ssm import LeptonLlamaIndexSSM
from openssm.integrations.lepton_ai.slm import SLM as LeptonSLM
from openssm.integrations.lepton_ai.ssm import SSM as LeptonSSM

from openssm.utils.config import Config
from openssm.utils.logs import Logs, logger, mlogger
from openssm.utils.utils import Utils
