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

## Capex signal
Total company capex was $2.9B in Q2 2026 (+8.3% YoY); Connectivity & Platforms segment capex rose 19.9% to $2.3B, "primarily reflecting higher spending on scalable infrastructure and customer premise equipment" — i.e., money is actively flowing into the kind of infrastructure HPE sells.

## Talking points to synthesize for the interview
1. **Lead with the AI Grid trial** — it's real, current, and names HPE ProLiant specifically. Ask where it stands today and what "graduating from trial to production" would require from an account team.
2. **Distinguish the two Comcast infrastructure narratives**: (a) the "smart, distributed access network" story (DOCSIS 4.0, Janus/DriveNets disaggregation) which is largely network/access-layer and not obviously an HPE compute play, vs. (b) the "AI at the edge / Comcast Business modernization" story, which is squarely where HPE's compute+networking+GreenLake+AI Grid pitch fits.
3. **Comcast Business, not just residential broadband, is probably the real growth surface** for new HPE business — AI-enabled networking, security, and edge compute are stated strategic priorities with money behind them.
4. Be honest that residential broadband subscriber losses create budget pressure company-wide — any HPE pitch likely needs a clear ROI/TCO story (efficiency, opex reduction, revenue-generating AI services) rather than pure top-line "more capacity" framing.

## Open questions to take into the interview (see your-questions.md for phrasing)
- Is the account being pursued as one Comcast-wide relationship, or split between Cable/Connectivity & Platforms vs. Comcast Business as distinct buying centers?
- Where does the AI Grid trial sit in the sales cycle today — is it a paid pilot, a co-marketing trial, or pre-commercial?
- How does the DriveNets/UfiSpace disaggregation strategy affect where HPE can and can't sell into the network core?
