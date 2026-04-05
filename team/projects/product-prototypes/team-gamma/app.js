var MODELS=[{id:"deepseek-r1",name:"DeepSeek-R1",org:"深度求索 DeepSeek",params:"671B MoE（活跃37B）",icon:"🧠",iconBg:"linear-gradient(135deg,#6366f1,#818cf8)",tags:[{l:"推理SOTA",c:"tag-green"},{l:"强化学习",c:"tag-blue"},{l:"开源",c:"tag-amber"}],benches:[{n:"AIME",v:"86%"},{n:"MATH-500",v:"97%"},{n:"MMLU",v:"90%"}],cats:["reasoning","code","data_analysis"],acc:["high"],bud:["free","cheap","unlimited"],score:{high:98,medium:90,low:75},code:'<span class="cm"># pip install openai</span>\n<span class="kw">from</span> <span class="fn">openai</span> <span class="kw">import</span> OpenAI\n\nclient = OpenAI(api_key=<span class="str">"your-key"</span>, base_url=<span class="str">"https://api.deepseek.com"</span>)\nresp = client.chat.completions.create(model=<span class="str">"deepseek-reasoner"</span>,\n  messages=[{<span class="str">"role"</span>:<span class="str">"user"</span>,<span class="str">"content"</span>:<span class="str">"请推导这道数学题..."</span>}])\n<span class="kw">print</span>(resp.choices[<span class="nb">0</span>].message.reasoning)',lang:"Python · DeepSeek API"},{id:"deepseek-v3",name:"DeepSeek-V3",org:"深度求索 DeepSeek",params:"671B MoE（活跃37B）",icon:"⚡",iconBg:"linear-gradient(135deg,#4f46e5,#6366f1)",tags:[{l:"MoE高效",c:"tag-green"},{l:"极低成本",c:"tag-cyan"},{l:"开源",c:"tag-amber"}],benches:[{n:"MMLU",v:"88%"},{n:"HumanEval",v:"90%"}],cats:["writing","code","long_context","customer_service"],acc:["high","medium"],bud:["free","cheap"],score:{high:94,medium:92,low:70},code:'<span class="cm"># pip install openai</span>\n<span class="kw">from</span> <span class="fn">openai</span> <span class="kw">import</span> OpenAI\n\nclient = OpenAI(api_key=<span class="str">"your-key"</span>, base_url=<span class="str">"https://api.deepseek.com"</span>)\nresp = client.chat.completions.create(model=<span class="str">"deepseek-chat"</span>,\n  messages=[{<span class="str">"role"</span>:<span class="str">"user"</span>,<span class="str">"content"</span>:<span class="str">"帮我写一封商务邮件..."</span>}])\n<span class="kw">print</span>(resp.choices[<span class="nb">0</span>].message.content)',lang:"Python · DeepSeek API"},{id:"qwen25-72b",name:"Qwen2.5-72B",org:"阿里巴巴通义实验室",params:"72B（7种规格）",icon:"🏮",iconBg:"linear-gradient(135deg,#f59e0b,#fbbf24)",tags:[{l:"128K上下文",c:"tag-cyan"},{l:"开源",c:"tag-amber"},{l:"中文领先",c:"tag-green"}],benches:[{n:"MMLU",v:"86%"},{n:"GSM8K",v:"95%"}],cats:["writing","customer_service","code","long_context"],acc:["high","medium"],bud:["free","cheap"],score:{high:92,medium:90,low:85},code:'<span class="cm"># pip install transformers accelerate</span>\n<span class="kw">from</span> <span class="fn">transformers</span> <span class="kw">import</span> AutoModelForCausalLM, AutoTokenizer\n\nmodel = AutoModelForCausalLM.from_pretrained(<span class="str">"Qwen/Qwen2.5-72B-Instruct"</span>, device_map=<span class="str">"auto"</span>)\ntok = AutoTokenizer.from_pretrained(<span class="str">"Qwen/Qwen2.5-72B-Instruct"</span>)\nmsgs = [{<span class="str">"role"</span>:<span class="str">"user"</span>,<span class="str">"content"</span>:<span class="str">"总结这份长文档"</span>}]\n<span class="kw">print</span>(model.generate(**tok(msgs, return_tensors=<span class="str">"pt"</span>)))',lang:"Python · HuggingFace"},{id:"minicpm-v45",name:"MiniCPM-V 4.5",org:"面壁智能 / 清华大学",params:"8B（端侧友好）",icon:"🐘",iconBg:"linear-gradient(135deg,#10b981,#34d399)",tags:[{l:"Nature论文",c:"tag-green"},{l:"中文OCR强",c:"tag-cyan"},{l:"端侧可运行",c:"tag-amber"}],benches:[{n:"MMMU",v:"~59%"},{n:"OCRBench",v:"开源领先"}],cats:["image","ocr","multimodal"],acc:["high","medium"],bud:["free","cheap"],score:{high:90,medium:88,low:82},code:'<span class="cm"># pip install transformers accelerate</span>\n<span class="kw">from</span> <span class="fn">transformers</span> <span class="kw">import</span> AutoModelForCausalLM\n<span class="kw">from</span> PIL <span class="kw">import</span> Image\n\nmodel = AutoModelForCausalLM.from_pretrained(<span class="str">"openbmb/MiniCPM-V-4_5"</span>, device_map=<span class="str">"auto"</span>)\nimg = Image.open(<span class="str">"invoice.png"</span>).convert(<span class="str">"RGB"</span>)\n<span class="kw">print</span>(model.chat(tokenizer=None, images=img, msgs=<span class="nb">0</span>))',lang:"Python · HuggingFace"},{id:"qwen25-vl72",name:"Qwen2.5-VL-72B",org:"阿里巴巴通义实验室",params:"72B（视频专家）",icon:"🎬",iconBg:"linear-gradient(135deg,#8b5cf6,#a78bfa)",tags:[{l:"小时级视频",c:"tag-blue"},{l:"超长视频",c:"tag-cyan"},{l:"多语言",c:"tag-green"}],benches:[{n:"MMMU",v:"68%"},{n:"Video-MME",v:"SOTA"}],cats:["video","image","multimodal"],acc:["high","medium"],bud:["cheap","unlimited"],score:{high:95,medium:88,low:72},code:'<span class="cm"># pip install qwen-vl-utils transformers</span>\n<span class="kw">from</span> <span class="fn">transformers</span> <span class="kw">import</span> Qwen2VLForConditionalGeneration\n\nmodel = Qwen2VLForConditionalGeneration.from_pretrained(<span class="str">"Qwen/Qwen2.5-VL-72B-Instruct"</span>, device_map=<span class="str">"auto"</span>)\nmsgs = [{<span class="str">"role"</span>:<span class="str">"user"</span>,<span class="str">"content"</span>:[{<span class="str">"type"</span>:<span class="str">"video"</span>,<span class="str">"video"</span>:<span class="str">"clip.mp4"</span>},{<span class="str">"type"</span>:<span class="str">"text"</span>,<span class="str">"text"</span>:<span class="str">"视频里发生了什么？"</span>}]}]\n<span class="kw">print</span>(model.generate(**processor(msgs)))',lang:"Python · HuggingFace"},{id:"llava-ov",name:"LLaVA-OneVision-1.5",org:"微软 & UW-Madison",params:"4B/8B（民主化）",icon:"🔮",iconBg:"linear-gradient(135deg,#0891b2,#22d3ee)",tags:[{l:"全开源",c:"tag-amber"},{l:"多图/视频",c:"tag-blue"},{l:"低成本",c:"tag-green"}],benches:[{n:"MMMU",v:"61%"},{n:"Video-MME",v:"开源领先"}],cats:["image","video","multimodal","ocr"],acc:["medium","low"],bud:["free"],score:{high:80,medium:86,low:88},code:'<span class="cm"># pip install transformers bitsandbytes</span>\n<span class="kw">from</span> <span class="fn">transformers</span> <span class="kw">import</span> AutoModelForCausalLM\n<span class="kw">from</span> PIL <span class="kw">import</span> Image\n\nmodel = AutoModelForCausalLM.from_pretrained(<span class="str">"lmms-lab/LLaVA-OneVision-1.5-8B-Instruct"</span>, device_map=<span class="str">"auto"</span>)\nimgs = [Image.open(<span class="str">"doc1.png"</span>), Image.open(<span class="str">"doc2.png"</span>)]\n<span class="kw">print</span>(model.chat(<span class="str">"对比这两份文档的差异"</span>, imgs))',lang:"Python · HuggingFace"},{id:"gemma3-27b",name:"Gemma 3-27B",org:"Google DeepMind",params:"27B（单GPU可跑）",icon:"💎",iconBg:"linear-gradient(135deg,#6366f1,#ec4899)",tags:[{l:"140+语言",c:"tag-cyan"},{l:"128K上下文",c:"tag-blue"},{l:"Gemini技术",c:"tag-amber"}],benches:[{n:"MMLU",v:"87%"}],cats:["writing","multimodal","long_context","customer_service"],acc:["high","medium"],bud:["free","cheap"],score:{high:88,medium:86,low:80},code:'<span class="cm"># pip install transformers</span>\n<span class="kw">from</span> <span class="fn">transformers</span> <span class="kw">import</span> AutoModelForCausalLM, AutoTokenizer\n\nmodel = AutoModelForCausalLM.from_pretrained(<span class="str">"google/gemma-3-27b-it"</span>, device_map=<span class="str">"auto"</span>)\ntok = AutoTokenizer.from_pretrained(<span class="str">"google/gemma-3-27b-it"</span>)\nmsgs = [{<span class="str">"role"</span>:<span class="str">"user"</span>,<span class="str">"content"</span>:<span class="str">"翻译这段英文为中文"</span>}]\n<span class="kw">print</span>(model.generate(**tok(msgs, return_tensors=<span class="str">"pt"</span>)))',lang:"Python · HuggingFace"}];

var state={step1:[],step2:null,step3:null};

function updateProgress(){
  var p=0;
  if(state.step1.length>0) p+=33;
  if(state.step2) p+=33;
  if(state.step3) p+=34;
  document.getElementById('progressFill').style.width=p+'%';
  document.getElementById('progressPct').textContent=p+'%';
}

function updateGoBtn(){
  var ready=state.step1.length>0&&state.step2&&state.step3;
  document.getElementById('goBtn').disabled=!ready;
  document.getElementById('goBtnText').textContent=ready?'开始智能选型':'完成以上选择 开始选型';
}

// Step 1: tag buttons (multi-select)
document.querySelectorAll('#tags1 .tag-btn').forEach(function(btn){
  btn.addEventListener('click',function(){
    var v=this.dataset.val;
    this.classList.toggle('selected');
    if(state.step1.includes(v)){
      state.step1=state.step1.filter(function(x){return x!==v;});
    } else {
      state.step1.push(v);
    }
    var cnt=state.step1.length;
    document.getElementById('sel1').textContent=cnt>0?cnt+'个已选':'可多选';
    document.getElementById('sn1').classList.toggle('done',cnt>0);
    updateProgress(); updateGoBtn();
  });
});

// Step 2: accuracy pills (single-select)
document.querySelectorAll('#accuracyPills .radio-pill').forEach(function(pill){
  pill.addEventListener('click',function(){
    document.querySelectorAll('#accuracyPills .radio-pill').forEach(function(p){p.classList.remove('selected');});
    this.classList.add('selected');
    state.step2=this.dataset.val;
    var labels={high:'🔬 最高',medium:'⚖️ 均衡',low:'🚀 够用'};
    document.getElementById('sel2').textContent=labels[state.step2];
    document.getElementById('sn2').classList.add('done');
    document.getElementById('step2').classList.add('active');
    updateProgress(); updateGoBtn();
  });
});

// Step 3: budget pills (single-select)
document.querySelectorAll('#budgetPills .radio-pill').forEach(function(pill){
  pill.addEventListener('click',function(){
    document.querySelectorAll('#budgetPills .radio-pill').forEach(function(p){p.classList.remove('selected');});
    this.classList.add('selected');
    state.step3=this.dataset.val;
    var labels={free:'🆓 免费',cheap:'💰 低成本',unlimited:'💎 不限'};
    document.getElementById('sel3').textContent=labels[state.step3];
    document.getElementById('sn3').classList.add('done');
    document.getElementById('step3').classList.add('active');
    updateProgress(); updateGoBtn();
  });
});

function runRecommendation(){
  var container=document.getElementById('resultsScroll');
  document.getElementById('emptyState').style.display='none';

  // Score and filter models
  var scored=MODELS.map(function(m){
    var catMatch=state.step1.some(function(c){return m.cats.indexOf(c)>-1;});
    var accMatch=m.acc.indexOf(state.step2)>-1;
    var budMatch=m.bud.indexOf(state.step3)>-1;
    var baseScore=m.score[state.step2]||0;
    var catBonus=catMatch?15:0;
    var finalScore=Math.min(100,baseScore+catBonus);
    return {m:m,score:finalScore,catMatch:catMatch,accMatch:accMatch,budMatch:budMatch};
  }).filter(function(x){return x.accMatch&&x.budMatch;})
    .sort(function(a,b){return b.score-a.score;})
    .slice(0,4);

  document.getElementById('resultCount').textContent=scored.length;
  var cats=state.step1.map(function(c){return({customer_service:'智能客服',writing:'内容文案',data_analysis:'数据分析',image:'图像',video:'视频',code:'代码',reasoning:'推理',long_context:'长文档',audio:'音频',multimodal:'多模态',ocr:'OCR',embedding:'嵌入'})[c]||c;}).join('、');
  var accs={high:'最高',medium:'均衡',low:'够用'};
  var buds={free:'免费',cheap:'低成本',unlimited:'不限'};
  document.getElementById('resultsMeta').textContent=cats+' · '+accs[state.step2]+' · '+buds[state.step3];

  container.innerHTML='';
  scored.forEach(function(item,idx){
    var m=item.m;
    var card=document.createElement('div');
    card.className='model-card';
    card.style.animationDelay=(idx*80)+'ms';

    var tagHTML=m.tags.map(function(t){return'<span class="model-tag '+t.c+'">'+t.l+'</span>';}).join('');
    var benchHTML=m.benches.map(function(b){return'<span class="bench-item"><span class="bn">'+b.n+':</span> <span class="bv">'+b.v+'</span></span>';}).join('');

    card.innerHTML='<div class="model-card-top"><div class="model-card-left"><div class="model-avatar" style="background:'+m.iconBg+'">'+m.icon+'</div><div class="model-info"><div class="model-name">'+m.name+'</div><div class="model-org">'+m.org+'</div><div class="model-tags">'+tagHTML+'</div></div></div><div class="model-match"><div class="match-score">'+item.score+'</div><div class="match-label">匹配度</div></div></div><div class="model-bench">'+benchHTML+'</div><div class="code-block"><div class="code-header"><span class="code-lang">&#128187; '+m.lang+'</span><button class="copy-btn" onclick="copyCode(this,\''+m.id+'\')">复制代码</button></div><div class="code-content" id="code-'+m.id+'">'+m.code.replace(/</g,'&lt;').replace(/>/g,'&gt;')+'</div></div>';

    container.appendChild(card);
  });
}

function copyCode(btn,id){
  var m=MODELS.find(function(x){return x.id===id;});
  if(!m) return;
  var plain=m.code.replace(/<[^>]+>/g,'').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
  navigator.clipboard.writeText(plain).then(function(){
    btn.textContent='已复制!';
    btn.classList.add('copied');
    setTimeout(function(){btn.textContent='复制代码';btn.classList.remove('copied');},2000);
  });
}
