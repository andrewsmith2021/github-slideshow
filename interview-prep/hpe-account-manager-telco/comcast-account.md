# Account Deep-Dive: Comcast

## The headline fact: HPE and Comcast are already working together

**HPE and Comcast have a live, named joint initiative right now.** This is the single best thing you can bring into the interview — it's specific, current (March 2026), and shows you understand exactly what HPE sells into this account today.

### HPE AI Grid + Comcast field trial (announced March 17, 2026)
- HPE launched **HPE AI Grid**, built on an NVIDIA reference architecture, to connect AI factories and distributed inference clusters across regional and "far-edge" sites.
- Stack: **HPE Juniper** multicloud routing + coherent optics for connectivity, cloud-native security/firewalls/WAN automation, plus **HPE ProLiant** edge and rack servers paired with NVIDIA accelerated computing (RTX PRO 6000 Blackwell GPUs, BlueField DPUs, Spectrum-X Ethernet, ConnectX SuperNICs).
- **Comcast is a named early adopter.** Comcast is running field trials putting NVIDIA GPUs in *regional facilities* — milliseconds from customers — instead of distant data centers, using Comcast's footprint of 65M+ homes/businesses.
- Named use cases in the trial:
  - **Small business "concierge" agent** — Personal AI's small language model + memory platform running on **HPE ProLiant servers**. This is the most direct compute win named in the announcement.
  - Personalized advertising agent (Decart real-time video models).
  - Low-latency online gaming.
- Comcast said lab testing showed strong performance; field trials are validating latency, power/cost efficiency, resiliency, scalability across its footprint, and real-world UX.
- Charter is reportedly pursuing a similar NVIDIA-based edge AI push — i.e., Comcast is not moving alone in the industry, but HPE is Comcast's named infrastructure partner for the AI Grid piece specifically.

**Why this matters for the interview:** you can say, concretely, "I know HPE ProLiant is already running in Comcast's edge AI field trial for the small-business concierge use case — I'd want to understand how that trial is progressing and where the next expansion points are" — that is a materially stronger answer than generic "I'd build relationships and learn the account" language.

### Where storage (Alletra Storage MP X10000) fits — HPE's general positioning, not a confirmed Comcast fact
The Comcast press release named ProLiant (compute) specifically; it did **not** name the X10000 or any storage product for Comcast's trial. But HPE's broader AI Grid/GreenLake messaging is explicit that storage is meant to be part of the same integrated, single-vendor-managed stack as compute and networking, not a separate sale:
- HPE has brought Juniper Data Center Networking into GreenLake and integrated Compute Ops Management so customers manage servers and network fabrics — and storage — from one interface, marketed as "unified management of compute, storage and networking."
- The Alletra Storage MP X10000's Data Intelligence Node (NVIDIA L40S-powered) does in-line metadata/vector-embedding enrichment — the exact function that feeds RAG/small-language-model inference, i.e., the same workload class as Comcast's concierge-agent use case. Storage becomes an active part of AI response speed/relevance, not passive capacity.
- Compute, network, and storage are each independently NVIDIA-certified, letting HPE claim a fully validated end-to-end stack rather than "storage integration is your problem."

**Why this framing would plausibly appeal to Comcast**, if it turns out storage is (or could be) in scope:
1. Comcast's trial is explicitly testing operational scale — "resiliency, scalability across Comcast's footprint" for potentially thousands of regional sites. Managing compute+network+storage as three separate vendor relationships at that scale is an operations burden a single GreenLake-managed stack reduces.
2. Comcast is already carrying disaggregation/integration risk elsewhere (the DIY, multi-vendor Janus/DriveNets/UfiSpace core build) — a pre-integrated, single-support edge AI stack is a natural complement, letting engineering effort go toward the network-core work that's strategically differentiated for Comcast, while edge AI infrastructure is comparatively turnkey.
3. AI Grid is explicitly built for multi-tenant, service-provider operating models — relevant because Comcast Business would be reselling these AI experiences to its own SMB customers, requiring carrier-grade multi-tenant isolation.
4. GreenLake's pay-per-use consumption matches Comcast's current capex posture (residential broadband under subscriber pressure, Business/AI as the funded growth bet) — letting spend scale with trial results rather than committing capex up front across many sites.

**How to use this in the interview:** raise it as your own informed hypothesis/question ("I'd want to understand whether storage is in scope for the AI Grid trial at Comcast, and if HPE's positioning it as part of one managed stack with compute and Juniper networking") rather than asserting it as a confirmed fact — see your-questions.md.

### A plausible edge deployment model: Data Fabric (x86) + Alletra Storage MP together
See company-and-role.md's storage section for the full explanation of HPE's Data Fabric + Alletra Storage MP combination. Applied to Comcast's scale problem specifically (potentially thousands of distributed regional/far-edge sites): it's not realistic to put a full Alletra MP X10000 appliance at every site. A more plausible architecture is **HPE Data Fabric software running on the same ProLiant nodes already doing AI inference at smaller/far-edge sites** (local, software-defined data services, no dedicated appliance), **federated via one global namespace with dedicated Alletra Storage MP capacity at larger regional hubs** for the heavier AI-ready object/file/vector-embedding work — all consumable via GreenLake. This is a reasoned hypothesis based on HPE's general portfolio positioning (confirmed current as of a May 2026 HPE announcement bundling Data Fabric and Alletra updates together), not a confirmed detail of Comcast's actual deployment — good material for a question to Bob/Imran, not a claim to assert as fact.

## What Comcast is doing with its own network (context, not necessarily HPE-sourced)

- **"Janus" initiative**: Comcast is virtualizing/disaggregating its network core using **DriveNets Network Cloud** software on **UfiSpace** white-box hardware. Trial started Atlanta, Sept 2024; since expanded nationwide. This shifts core routing/switching/transport functions from proprietary hardware onto disaggregated, cloud-style infrastructure.
  - *Competitive read:* this is a white-box/disaggregated approach — a different philosophy than a fully integrated vendor stack. Worth asking internally whether HPE/Juniper is positioned as complementary here (e.g., optics/routing at the edge, or compute elsewhere) or effectively displaced by DriveNets+white-box in that specific layer. Don't guess out loud in the interview — ask Bob/Imran (see your-questions.md).
- **DOCSIS 4.0**: Comcast is a lead operator (10+ US markets) delivering multi-gig symmetrical speeds — first-in-world DOCSIS 4.0 deployment claim. Also expanding fiber-to-the-premises: up to 10 Gbps residential, 100 Gbps business, 400 Gbps for certain large business customers.
- **Broadband subscriber trend**: domestic residential broadband had a net loss of ~167,000 customers in Q2 2026 (an improvement of 34,000 YoY) — the core residential business is under pressure; 45% of the base is now on gigabit+ tiers.

## Where the growth (and likely budget) actually is: Comcast Business

This is probably the more relevant growth surface for an Account Manager focused on new business, not just defending an installed base:

- **Comcast Business is explicitly repositioning** from a connectivity-led ISP to a "solutions- and platform-oriented partner" for enterprise customers (strategy shift accelerating since 2025).
- Financials: Business Services revenue +6% YoY; the Connectivity division within it grew 5.7% to $2.6B with a 55.9% EBITDA margin (Q1 2026) — a healthy, growing, high-margin unit.
- Stated strategic priorities: **AI-enabled networking, cybersecurity, and edge compute** — directly in HPE's wheelhouse (compute, networking/Juniper, GreenLake, AI Grid).
- Enterprise customers are now spending **3x more on value-added services** (mobility, SD-WAN, security, unified comms) than on core connectivity, versus 2023 — cross-sell motion, not just pipe-selling.
- New **T-Mobile MVNO agreement** to grow wireless revenue from larger business customers in 2026.
- Ambition: Comcast Business is aiming past $10B in annual revenue with sustained double-digit enterprise growth, via acquisitions, global partnerships, and portfolio expansion.
- Comcast Business already lists **HPE Aruba** among its SD-WAN technology partners (alongside Versa, Fortinet, Cisco) — so there's an existing multi-vendor relationship in networking, not a clean-sheet sell.

## Capex vs. opex — the real argument, since Comcast is a capex-preferring operator

**The raw signal:** total company capex was $2.9B in Q2 2026 (+8.3% YoY); Connectivity & Platforms segment capex rose 19.9% to $2.3B, "primarily reflecting higher spending on scalable infrastructure and customer premise equipment" — money is actively flowing into the kind of infrastructure HPE sells.

**But don't assume "just use GreenLake" is automatically credible.** Comcast has historically run higher capital intensity than peers (e.g., notably higher than Sky's), consistent with a cable operator that owns and depreciates long-lived plant (HFC, DOCSIS equipment, fiber) over decades — the classic capex logic: capitalize infrastructure with a long useful life, depreciate predictably, and get rewarded by investors for visible capital discipline against subscriber/revenue growth. That's a real, deep-seated preference, not something to talk past.

**Why AI/GPU infrastructure specifically breaks that logic, and opens the door to a genuine exception:**
1. **GPU economic life is nothing like cable plant life.** Frontier GPU clusters have an assumed ~3-year economic life, with roughly 78% of a GPU's economic capacity exhausted within those first 3 years — a $100 investment in frontier AI compute is worth about $22 in economically competitive capacity by year three. Capitalizing an asset that's largely obsolete before a normal depreciation schedule even finishes is a real financial risk (impairment exposure), the opposite of how capex logic works for network gear with 7-10+ year useful life.
2. **Distributed edge sites have a real utilization problem.** Telco/cable GPUaaS deployments face a "utilization trap" — GPUs spread across many regional facilities (exactly Comcast's AI Grid model) struggle to hit the 60-70%+ utilization hyperscalers achieve at centralized scale. Owning fast-depreciating, likely-underutilized hardware at potentially thousands of sites is a bad capital bet; a consumption model shifts that utilization risk toward the vendor rather than stranding it on Comcast's balance sheet.
3. **It's a field trial against an unproven demand curve.** Comcast has decades of forecasting experience for broadband subscriber growth, essentially none yet for edge-AI inference demand. Consumption spend lets them validate the model (and the right GPU generation/config) before committing capital to a use case, or a hardware generation, that might be wrong in 18 months.
4. **Balance sheet optics matter more right now, not less.** Residential broadband is losing subscribers and free cash flow is under investor scrutiny (see above). Adding a new debt-funded asset class for an unproven initiative is a harder internal sell than a period of opex-based validation, especially while Comcast Business (the funded growth bet) is the unit actually driving this.

**The nuance that changes the framing, though:** per company-and-role.md's GreenLake section, the consumption-billing decision and the management-plane decision are actually separable. Compute Ops Management (and GreenLake generally) can manage hardware Comcast owns outright, and can itself be licensed upfront rather than metered. So **even if Comcast's capex-preferring culture wins out on how the AI Grid hardware gets financed — especially once the pilot is proven and they're ready to commit — they'd likely still want GreenLake for the separate, genuinely capex-agnostic problem of operating potentially thousands of distributed inference sites as one coordinated system.** That's arguably the stronger, more durable pitch: not "use GreenLake because opex beats capex," but "use GreenLake's management layer regardless of how you finance the boxes, because managing this many distributed sites without it is an operational risk on its own."

**The sharper question to ask Bob/Imran isn't "would Comcast use GreenLake" — it's "how is GreenLake actually structured for the AI Grid trial: pure consumption, a committed-use structure easing toward capex as it matures, or hardware Comcast owns with just the management layer subscribed?"** That shows you understand the objection isn't really "capex vs. opex," it's "unproven vs. proven, and financing vs. management are two different questions."

**Confirmed vs. not:** none of the public reporting on Comcast's AI Grid trial mentions GreenLake, consumption billing, or how the trial is commercially structured — see the "Is GreenLake part of the current field trial" question already flagged in your-questions.md. Everything above is reasoned positioning to raise as an informed question, not a fact to assert.

## Talking points to synthesize for the interview
1. **Lead with the AI Grid trial** — it's real, current, and names HPE ProLiant specifically. Ask where it stands today and what "graduating from trial to production" would require from an account team.
2. **Distinguish the two Comcast infrastructure narratives**: (a) the "smart, distributed access network" story (DOCSIS 4.0, Janus/DriveNets disaggregation) which is largely network/access-layer and not obviously an HPE compute play, vs. (b) the "AI at the edge / Comcast Business modernization" story, which is squarely where HPE's compute+networking+GreenLake+AI Grid pitch fits.
3. **Comcast Business, not just residential broadband, is probably the real growth surface** for new HPE business — AI-enabled networking, security, and edge compute are stated strategic priorities with money behind them.
4. Be honest that residential broadband subscriber losses create budget pressure company-wide — any HPE pitch likely needs a clear ROI/TCO story (efficiency, opex reduction, revenue-generating AI services) rather than pure top-line "more capacity" framing.

## Open questions to take into the interview (see your-questions.md for phrasing)
- Is the account being pursued as one Comcast-wide relationship, or split between Cable/Connectivity & Platforms vs. Comcast Business as distinct buying centers?
- Where does the AI Grid trial sit in the sales cycle today — is it a paid pilot, a co-marketing trial, or pre-commercial?
- How does the DriveNets/UfiSpace disaggregation strategy affect where HPE can and can't sell into the network core?
